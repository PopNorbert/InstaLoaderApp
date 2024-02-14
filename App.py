class App:
    def __init__(self, controller):
        self.controller = controller
        self.run()

    def run(self):
        print("\n1 - get unfollowers\n")
        match int(input(">")):
            case 1:
                user = input("Username: ")
                res = self.controller.getUnfollowers(user)
                with open("out.txt")as o:
                    for a in res:
                        o.write(f"{a}\n")



