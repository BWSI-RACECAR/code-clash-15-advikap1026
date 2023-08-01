class Solution:
    def interval_scheduling(self, intervals):
            #type intervals: list of int tuples
            #return type: list of int tuples
            
            #TODO: Write code below to return an int tuples list with the solution to the prompt.
            print("intervals: " + str(intervals))
            intervals.sort()
            #intervas = sorted(intervals, key = lambda x:x[1])
            answer = []
            answer.append(intervals[0]) 

            count = 0 
            for i in range (len(intervals)):
                 if i == 0: 
                      continue 
                 start_time = intervals[i][0]
                 end_time = intervals[i][1]
                 previous_end_time = intervals[count][1]
                 previous_start_time = intervals[count][0]
                 if start_time >= previous_end_time: 
                      answer.append(intervals[i])
                      count = count + 1
            print("answer: " + str(answer))
            return answer 
                      
                 
                
            pass



def main():
    string = input()
    string = string.replace(" ", "")  # Remove any whitespace in the string
    string = string.replace("),", ")|")  # Replace the comma between tuples with a custom separator
    
    list_from_string = string.split("|")  # Split the string into individual tuple strings
    
    # Convert the tuple strings to actual tuples
    result = [eval(tuple_str) for tuple_str in list_from_string]

                
    tc1= Solution()
    ans=tc1.interval_scheduling(result)
    print(ans)
    
if __name__ == "__main__":
    main()