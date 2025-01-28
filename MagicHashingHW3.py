class Student:
    def __init__(self,id, fn, ln, gl, gpa):
        self.id = id #int
        self.first_name = fn #string
        self.last_name = ln #string
        self.grade_level = gl #int
        self.gpa = gpa #float
    
    def __hash__(h):
        attributes = vars(h)
        vals = list(attributes.values())
        results = []
        for i in range(len(vals)):
            if type(vals[i]) == int:
                print("int")
                results.append(vals[i] % 13)
            if type(vals[i]) == str:
                print("string")
                result = 0
                for char in vals[i]:
                    result = result * 31 + ord(char)
                results.append(result)
            if type(vals[i]) == float:
                print("float")
                results.append(int(vals[i]*100) % 13)
        print(results)
        return 2
        #get the hash of the student

def main():
    h = Student(16,"Nicolas","White",11,4.0)
    print(hash(h))

if __name__ == "__main__":
    main()