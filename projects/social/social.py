import random 
import math
from util import Queue, Stack

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0 # id of the last user added
        self.users = {} # {1: User("1"), 2: User("2")...}
        self.friendships = {} # {1: {2, 3, 4}}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        # add users
        for i in range(num_users):
            self.add_user(f"User {i}")
        
        # Create friendships
        # Generate all the possible friendships and put them into an array
        # 3 users (0, 1, 2) and bidirectional friendships
        # [(0, 1), (0, 2), (1, 2)]
        possible_friendships = []
        for user_id in self.users:
            # to prevent duplicate friendships increment by 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle friendship array
        # [(1, 2), (0, 1), (0, 2)]
        random.shuffle(possible_friendships)

        
        # Take the first num_users * avg_friendships / 2 and that will be the friendships for that graph
        for i in range(math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """        
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()

        queue.enqueue([user_id])

        while queue.size() > 0:
            path = queue.dequeue()
            currNode = path[-1]
            if currNode not in visited:
                visited[currNode] = path
                for friend in self.friendships[currNode]:
                    queue.enqueue(path + [friend])
        return visited

        # O(n^2) because of double for loop
        # visited = {} # dict for mapping form node id --> [path from user_id]
        # queue = deque() # need this for a bft
        # queue.append([user_id])
        # while len(queue) > 0:
        #     currPath = queue.popleft()
        #     currNode = currPath[-1]
        #     visited[currNode] = currPath # bft gaurantees us tht this is the shortest path to currNode from user_id
        #     for friend in self.friendships[currNode]:
        #         if friend not in visited:
        #             newPath = currPath.copy()
        #             newPath.append(friend)
        #             queue.append(newPath)
        # return visited

def populate_graph_linear(self, num_users, avg_friendships):
    # Keep randomly making friendship until we've made the right amoutn
    # randomly select two vertices to become friends
    # if it's a success, then increment num of friendships made
    # else try again
    self.last_id = 0
    self.users = {}
    self.friendships = {}

    for i in range(0, num_users):
        self.add_user(f"User {i}")

    target_friendships = num_users * avg_friendships
    total_friendships = 0
    collisions = 0
    # runtime 0(num targeted friendships)
    while total_friendships < target_friendships:
        user_id = random.randint(1, self.last_id)
        friend_id = random.randint(1, self.last_id)
        if self.add_friendship_linear(user_id, friend_id):
            total_friendships += 2
        else:
            collisions += 1
    print(f"collisions: {collisions}")

# returns true if making friendship was a success
def add_friendship_linear(self, user_id, friend_id):
    if user_id == friend_id:
        return False
        # we don't want to make a friendship is it already exists
    elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
        return False
    else:
        self.friendships[user_id].add(friend_id)
        self.friendships[friend_id].add(user_id)
        return True

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f'friendships: {sg.friendships}')
    connections = sg.get_all_social_paths(1)
    print(f'connections: {connections}')
