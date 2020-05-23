
import os
import numpy as np
import argparse
from collections import namedtuple
from my_queue import PriorityQueue

import random


Results = namedtuple('Results', 'Number_of_tested, Number_of_arrived_but_left, Time_of_treatment_finish')

def generate_time(exp_variable):
    """ Will generate the next event time based on exponential distribution"""
    # generate random variable
    ran_var = random.uniform(0, 1)

    # generate arrival time
    arr_time = - (1/exp_variable) * np.log(ran_var)
    return arr_time


class Event(object):
    """The general class for any event"""
    def __init__(self, time):
        self.time = time


class Arrival(Event):
    """The arrival event"""
    def __init__(self, time, location):
        super().__init__(time)
        self.type = "arrival"
        self.location = location

    def __str__(self):
        return f"Event : {self.type}, time : {self.time}, location: {self.location}\n" 

class Test_taken(Event):
    """The test taken event"""
    def __init__(self, time, location):
        super().__init__(time)
        self.type = "test_taken"
        self.location = location  # index of test station

    def __str__(self):
        return f"Event : {self.type}, time : {self.time}, location: {self.location}\n" 

class Environment():
    def __init__(self, num_test_points : int, probs : []):
        self.current_time : int = 0
        self.current_states = {}        # number of people in each test place

        for n in range(num_test_points):
            self.current_states[n] = 0

        self.people_tested : int = 0
        self.people_came_and_left : int = 0
        self.probs = probs
        
    def __str__(self):
        return f"Current time : {self.current_time}, Tested : {self.people_tested}, Came & Left  :{self.people_came_and_left}"

    def process_event(self, next_event : Event):
        """ change the environment based on the event that happened"""
        
        # if the event is arrival, use the probabilities to see if person enters the queue
        self.current_time = next_event.time

        # print(self)

        if next_event.type == "arrival":
            prob_to_stay = self.probs[self.current_states[next_event.location]]
            ran_var = random.uniform(0, 1)

            if ran_var < prob_to_stay:
                # the visitor stayed for test
                self.current_states[next_event.location] += 1
                return True
            else:
                self.people_came_and_left += 1
                return False
                

        else:
            # test taken
            self.current_states[next_event.location] -= 1
            self.people_tested += 1
            return True


        # if the event is test_taken, just increase test taken cases



        



class Simulator():
    def __init__(self):
        self.time_limit : int = None
        self.num_test_points : int = None
        self.probs = []
        self.priority_q = PriorityQueue()

        self.history_q = PriorityQueue()

        
    def load_data(self, *argv):
        self.time_limit         = argv[0]
        self.num_test_points    = argv[1]
        self.lambda_var         = argv[2]
        self.mu_var             = argv[3]
        self.probs              = argv[4:]

    def run_sim(self):

        # 1. init the environment
        env = Environment(sim.num_test_points, sim.probs)

        # init : 
        # generate arrival for each test point
        separate_arrival_rate =  self.lambda_var / self.num_test_points

        for tp_idx in range(self.num_test_points):
            new_arrival = generate_time(separate_arrival_rate)
            arrival_time = env.current_time + new_arrival
            new_event = Arrival(arrival_time, tp_idx)

            # add to priority queue
            self.priority_q.insert(new_event)
            self.history_q.insert(new_event)

        #print(self.priority_q)

        # jump to the next event 
        while self.priority_q.isEmpty() == False:

            # go to the next event
            next_event = self.priority_q.pop()

            # increase the number of patients in the test system due to the probabilities
            event_happened = env.process_event(next_event)

            # if the event was arrival, 
            # if the event was test_taken, generate new event 'test_taken' for same test point

            if next_event.type == "arrival":
                # generate new arrival - they happen all the time
                new_arrival_time        = generate_time(separate_arrival_rate) + env.current_time
                tp_idx                  = next_event.location
                new_event               = Arrival(new_arrival_time, tp_idx)


                if new_arrival_time < sim.time_limit:
                    self.priority_q.insert(new_event)
                    self.history_q.insert(new_event)

                # if the arrived visitor is the only visitor, add the test_taken event
                if event_happened and env.current_states[next_event.location] == 1:
                    new_test_taken_time     = generate_time(self.mu_var) + env.current_time
                    tp_idx                  = next_event.location
                    new_event               = Test_taken(new_test_taken_time, tp_idx)

                    self.priority_q.insert(new_event)
                    self.history_q.insert(new_event)

                

            elif next_event.type == "test_taken":
                # new test_taken event - take another test if there are visitors   
                if env.current_states[next_event.location] > 0:
                    # there are patients
                    new_test_taken_time     = generate_time(self.mu_var) + env.current_time
                    tp_idx                  = next_event.location
                    new_event               = Test_taken(new_test_taken_time, tp_idx)

                    self.priority_q.insert(new_event)
                    self.history_q.insert(new_event)

            


        results = Results(env.people_tested, env.people_came_and_left, env.current_time)
        return results
        



if __name__ == "__main__":
    sim = Simulator()
    sim.load_data(1000, 2, 40, 25, 1, 0.5, 0.25, 0)
    
    results = sim.run_sim()

    print(f"\nResults are: {results}")
