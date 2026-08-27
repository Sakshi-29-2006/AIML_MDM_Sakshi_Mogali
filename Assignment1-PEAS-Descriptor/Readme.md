# PEAS Descriptor using Vacuum Cleaner Intelligent Agent

## Overview

This practical demonstrates the **PEAS (Performance Measure, Environment, Actuators, Sensors)** framework using a **Vacuum Cleaner Intelligent Agent**.

The agent is implemented in **Prolog** and operates in an environment containing three connected rooms. It detects dirty rooms, cleans them, moves to adjacent dirty rooms, and stops when all rooms are clean.

## Objectives

- To understand the concept of an Intelligent Agent.
- To study the PEAS framework for describing a task environment.
- To identify the Performance Measure, Environment, Actuators, and Sensors of a Vacuum Cleaner Agent.
- To implement a simple rule-based Vacuum Cleaner Intelligent Agent using Prolog.

## PEAS Description

**Performance Measure** - Clean all rooms with minimum actions and movement 
**Environment** - Three connected rooms: A, B, and C 
**Actuators** - Clean, Move, Stop 
**Sensors** - Detect the current location and whether a room is dirty 

## Environment

The vacuum cleaner operates in three rooms with the following connections:

```text
A <----> B <----> C