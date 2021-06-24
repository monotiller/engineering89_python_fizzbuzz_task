import list


class FizzBuzz:
    def play(self):
        for counter in range(100):  # counting from 0 to the limit
            output = ""  # Preparing the output which we will modify based on whether or not the number will be Fizz or Buzz
            for number in list.fb_dict().keys():  # Scans through the dictionary for matching keys
                if counter % number == 0:
                    output += list.fb_dict()[number]  # Adds the word to the current output
                    return output
            if output == "":  # If the output is still empty...
                output = counter  # Add the current counter value to it...
            return output  # Print the output for this loop