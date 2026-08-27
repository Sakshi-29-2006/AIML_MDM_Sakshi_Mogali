% Student Burnout Risk Expert System

% Facts
student(sakshi).

sleep(sakshi, 5).
study(sakshi, 9).
stress(sakshi, high).
focus(sakshi, low).
screen(sakshi, 8).
breaks(sakshi, 1).
assignments(sakshi, 5).

% Rules for identifying risk factors

low_sleep(S) :-
    sleep(S, H),
    H < 6.

overstudy(S) :-
    study(S, H),
    H > 8.

high_screen(S) :-
    screen(S, H),
    H > 6.

few_breaks(S) :-
    breaks(S, B),
    B < 3.

heavy_work(S) :-
    assignments(S, N),
    N > 3.

% Burnout rules

high_risk(S) :-
    low_sleep(S),
    overstudy(S),
    stress(S, high).

severe_risk(S) :-
    high_risk(S),
    high_screen(S),
    few_breaks(S).

% Diagnosis

diagnosis(S, severe) :-
    severe_risk(S).

diagnosis(S, high) :-
    high_risk(S),
    \+ severe_risk(S).

diagnosis(S, moderate) :-
    stress(S, high),
    \+ high_risk(S).

diagnosis(S, healthy) :-
    sleep(S, H),
    H >= 7,
    study(S, T),
    T =< 8,
    stress(S, low).
% Expert recommendations

advice(S, 'Get at least 7 hours of sleep') :-
    low_sleep(S).

advice(S, 'Reduce continuous study hours') :-
    overstudy(S).

advice(S, 'Reduce unnecessary screen time') :-
    high_screen(S).

advice(S, 'Take regular short breaks') :-
    few_breaks(S).

advice(S, 'Prioritize pending assignments') :-
    heavy_work(S).

advice(S, 'Use focused study techniques') :-
    focus(S, low).

% Display advice

show_advice(S) :-
    advice(S, A),
    write('- '),
    write(A),
    nl,
    fail.

show_advice(_).


% Run the expert system

run :-
    student(S),

    diagnosis(S, D),

    write('Student Burnout Expert System'), nl,
    write('Student: '), write(S), nl,
    write('Burnout Risk: '), write(D), nl,
    nl,

    write('Recommendations:'), nl,
    show_advice(S).

