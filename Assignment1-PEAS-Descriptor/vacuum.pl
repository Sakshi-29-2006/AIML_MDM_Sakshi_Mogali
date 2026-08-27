:- dynamic dirty/1.
:- dynamic vacuum_location/1.

% Define rooms
room(a).
room(b).
room(c).

% Define adjacent rooms
adjacent(a, b).
adjacent(b, a).
adjacent(b, c).
adjacent(c, b).

% Initial dirty rooms
dirty(a).
dirty(b).
dirty(c).

% Initial vacuum location
vacuum_location(a).

% Select clean action
action(clean) :-
    vacuum_location(Room),
    dirty(Room).

% Select move action
action(move(ToRoom)) :-
    vacuum_location(CurrentRoom),
    adjacent(CurrentRoom, ToRoom),
    dirty(ToRoom).

% Select stop action when all rooms are clean
action(stop) :-
    \+ dirty(_).

% Perform cleaning
perform(clean) :-
    vacuum_location(Room),
    dirty(Room),
    retract(dirty(Room)),
    format("Cleaning room ~w...~n", [Room]).

% Perform movement
perform(move(ToRoom)) :-
    vacuum_location(CurrentRoom),
    retract(vacuum_location(CurrentRoom)),
    assertz(vacuum_location(ToRoom)),
    format("Moving from room ~w to room ~w...~n", [CurrentRoom, ToRoom]).

% Perform stop
perform(stop) :-
    format("All rooms are clean. Stopping...~n", []).

% Run the agent until all rooms are clean
start :-
    action(Action),
    perform(Action),
    Action \= stop,
    start.

start :-
    action(stop),
    perform(stop).
