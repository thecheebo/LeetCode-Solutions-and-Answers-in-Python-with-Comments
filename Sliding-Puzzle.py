class Solution(object):
    def slidingPuzzle(self, board):
        
        # List out posible moves in Dictionary
        moves = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}
        
        # Create set to check if the boardstate has been checked previously
        seenSet = set()
        
        count = 0
        
        # Stringify the boardstate
        solution = "".join(str(col) for row in board for col in row)
        
        # Create a Tuple of a Board State and the index of Zero
        q = [(solution, solution.index("0"))]
        
        # Keep looping while there are unseen boardstates
        while q:
            
            # Create an empty Queue
            new = []
            
            # Iterate through the current board:
            for s, i in q:
                
                # Add string, it represents the state of the board to the set of boards seen
                seenSet.add(s)

                # Checks if the board is solved
                if s == "123450":
                    return count

                # List Comp for the string, turning the board state into one string
                arr = [c for c in s]

                # Iterate through the possible index of the next location of zero
                for move in moves[i]:
                    
                    # Copy the array of the current board
                    new_arr = arr[:]
                    
                    # Swap locations of where the current zero is with potential move
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    
                    # Concactenate back the new potential board states into a string to add the queue
                    new_string = "".join(new_arr)
                    
                    # If the new set combination hasnt been seen, add to queue along with zero position
                    if new_string not in seenSet:
                        new.append((new_string, move))
            
            # Up the count of moves
            count +=1
            
            # Update Q to the new moves to be checked
            q = new
        
        #iterate through the entire possible combinations of moves and have an impossible board state return -1
        return -1
        
