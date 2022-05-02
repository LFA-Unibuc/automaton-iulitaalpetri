class Automaton:

    def __init__(self, config_file):
        self.config_file = config_file

        self.sigma=[]
        self.stari=[]
        self.tranz=[]

        with open(self.config_file) as f:

            linie= f.readline().strip()
            #sigma
            while  linie.lower()!= "end":

                if linie[0]=='#' or ("..." in linie) or (":" in linie):
                    linie = f.readline().strip()

                    continue
                else:
                    self.sigma.append(linie)
                    linie = f.readline().strip()




            #stari

            linie= f.readline().strip()


            while linie.lower() != "end":

                if linie[0] == '#' or ("..." in linie) or (":" in linie):
                    linie = f.readline().strip()
                    continue
                else:
                    tuplu=linie.split(",")
                    tuplu[0]= tuplu[0].strip()
                    if len(tuplu)> 1:tuplu[1]= tuplu[1].strip()
                    self.stari.append(tuplu)
                    linie = f.readline().strip()

            #tranz
            linie = f.readline().strip()

            while linie.lower()!="end":
                if linie[0] == "#" or ("..." in linie) or (":" in linie):
                    linie = f.readline().strip()
                    continue
                else:
                    x= linie.split(",")
                    x[0]= x[0].strip()
                    x[1]= x[1].strip()
                    x[2]= x[2].strip()
                    self.tranz.append(x)

                    linie = f.readline().strip()

        print("sigma:",self.sigma)
        print("tranz:", self.tranz)
        print(self.stari)




    def validate(self):
        # check for unique start state and final state
        st_init_sau_fin=[t[1] if len(t)> 1 else "" for t in self.stari]

        if st_init_sau_fin.count("S") > 1:
            raise Exception("Only one starting state allowed!")

        # check transitions
        for transition in self.tranz:

            valid_states = [state[0] for state in self.stari]

            if transition[0] not in valid_states or transition[2] not in valid_states or transition[1] not in self.sigma:
                raise Exception("Transition contains invalid words or states!")
        return (True, st_init_sau_fin)
    def retsigma(self):
        return self.sigma
    def retstates(self):
        return self.stari
    def rettransitions(self):
        return self.tranz
    def create_function(self):
        x= {tuple([tr[0].strip(), tr[1].strip()]): tr[2].strip() for tr in self.tranz}

        return x

    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration

        If the input is rejected, the method raises a
        RejectionException.
        """
        pass




if __name__ == "__main__":
    a = Automaton('input.txt')

    print(a.validate())

