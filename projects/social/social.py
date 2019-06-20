import random


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f'User {i+1}')
        # Create friendships
        potentialFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                potentialFriendships.append((userID, friendID))
        random.shuffle(potentialFriendships)
        first = True
        keys = []
        for friendship in potentialFriendships[:20]:
            self.addFriendship(friendship[0], friendship[1])

    def bfs(self, starting_vertex, search_vertex):
        Q = Queue()
        visited = set()
        Q.enqueue([starting_vertex])
        while Q.size() > 0:
            path = Q.dequeue()
            v = path[-1]
            visited.add(v)
            if v not in visited:
                visited.add(v)
                if v == search_vertex:
                    return path
                for neighbor in self.friendships[v]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    Q.enqueue(new_path)

    def getAllSocialPaths(self, userID):
        print(f'UserId {userID}')
        visited = {}
        count = 1
        for i in range(1, 11):
            visited[i] = self.bfs(userID, i)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
