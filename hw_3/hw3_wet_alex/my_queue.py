

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ''.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def insert(self, event): 
        self.queue.append(event) 
  
    # for popping an element based on Priority 
    def pop(self): 
        try: 
            min_idx = 0
            for i in range(len(self.queue)): 
                if self.queue[i].time < self.queue[min_idx].time: 
                    min_idx = i 
            min_time_event = self.queue[min_idx] 
            del self.queue[min_idx] 
            return min_time_event 
        except IndexError: 
            print() 
            exit() 