# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
import time
from rclpy.node import Node
from rclpy.action import ActionServer
from std_msgs.msg import String
from holon_msgs.msg import AdjacencyList
from holon_msgs.action import Transport 


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('R_KR10')
        self.publisher_ = self.create_publisher(AdjacencyList, 'graph_node_network', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        #Action server declaration
        self._action_server = ActionServer(self,Transport,'transport_request',self.transport_callback,goal_callback=self.goal_parse_msg)

        self.graph = AdjacencyList()
        self.graph.node = 3
        self.graph.adjacent = [2,4,5,6]

    def timer_callback(self):
        self.publisher_.publish(self.graph)
        #self.get_logger().info('Publishing: "%x" and "%x"' % (self.graph.node self.graph.adjacent))
    
    #--------- Action Server Functions Start---------------------
    def goal_parse_msg(self,goal_request):
        self.get_logger().info('Transport request from node %d to %d' % (goal_request.a,goal_request.b))
        if ((goal_request.a == 2 and goal_request.b == 3) or (goal_request.a == 3 and goal_request.b == 2) or (goal_request.a == 3 and goal_request.b == 4)or (goal_request.a == 4 and goal_request.b == 3) or (goal_request.a == 3 and goal_request.b == 5)or (goal_request.a == 5 and goal_request.b == 3) or (goal_request.a == 3 and goal_request.b == 6)or (goal_request.a == 6 and goal_request.b == 3)):
            print("Accepting Goal")
            return rclpy.action.GoalResponse(2)
        else:
            print("Declined Goal")
            return rclpy.action.GoalResponse(1)

    def transport_callback(self, goal_handle):

        result = Transport.Result()
        print(goal_handle.request.a)
        nodea = goal_handle.request.a
        nodeb = goal_handle.request.b
        print(nodea)
        if nodea == 2 and nodeb == 3: 
            self.get_logger().info('Transporting to Node 3...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        if nodea == 3 and nodeb == 2: 
            self.get_logger().info('Transporting to Node 2...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        if nodea == 3 and nodeb == 4: 
            self.get_logger().info('Transporting to Node 4...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        if nodea == 4 and nodeb == 3: 
            self.get_logger().info('Transporting to Node 3...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        if nodea == 3 and nodeb == 5: 
            print("hi")
            self.get_logger().info('Transporting to Node 5...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        if nodea == 5 and nodeb == 3: 
            print("hi")
            self.get_logger().info('Transporting to Node 3...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        if nodea == 3 and nodeb == 6: 
            self.get_logger().info('Transporting to Node 6...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        if nodea == 6 and nodeb == 3: 
            self.get_logger().info('Transporting to Node 3...')
            feedback_msg = Transport.Feedback()
            feedback_msg.percent = 0
            for i in range(1, 100):
                feedback_msg.percent = i
                goal_handle.publish_feedback(feedback_msg)
                time.sleep(.05)
            goal_handle.succeed()
            result.completion = True
            return result
        else:
            print("hey")
            goal_handle.abort()
            result.completion = False
            return result 

    
    #----------Action Server Functions End------------------------

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
