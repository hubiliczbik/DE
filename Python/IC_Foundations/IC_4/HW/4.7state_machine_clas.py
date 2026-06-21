from datetime import datetime
class InvalidTransition(Exception):
    pass

class StateMachine:
    def __init__(self, initial_state, transitions):
        self.initial_state = initial_state
        self.state = initial_state
        self.transitions = transitions
        self.history = []

    def transition(self, action):
        current_state = self.state
        if current_state not in self.transitions or action not in self.transitions[current_state]:
            raise InvalidTransition(f"Invalid transition")

        next_state = self.transitions[current_state][action]
        timestamp = datetime.now()
        self.history.append((current_state, next_state, timestamp))
        self.state = next_state
        return self.state

class TrafficLight(StateMachine):
    def __init__(self):
        transitions = {
            "red": {
                "start": "green"
            },
            "green": {
                "caution": "yellow"
            },
            "yellow": {
                "stop": "red"
            }
        }
        super().__init__("red", transitions)
    
    def start(self):
        return self.transition("start")
    
    def caution(self):
        return self.transition("caution")
    
    def stop(self):
        return self.transition("stop")

light = TrafficLight()

print(light.state) 
print(light.start())  
print(light.caution()) 
print(light.stop())  
print(light.history)

        
        

        