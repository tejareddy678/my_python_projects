import random as rd
person_id_list = set()
voter_id_list = set()
candidate_id_list = set()
vote_casted = set()
election_status = False
candidate_votes = {}

class Person:
    def __init__(self,name : str,age : int,gender : str):
        self.name = name
        self.age = age
        self.gender = gender
        self._person_id = rd.randrange(100, 999)
        while(self._person_id in person_id_list):
            self._person_id = rd.randrange(100, 999)
        person_id_list.add(self._person_id)

    def profile(self):
        print(f"Person_id : {self._person_id}\nName : {self.name}\nage : {self.age} years\nGender : {self.gender}")

class Voter(Person):
    def __init__(self,name : str,age : int,gender : str,):
        super().__init__(name,age,gender)
        self._is_registered_for_election = False
        self._voter_id = rd.randrange(1000000000,9999999999)
        while(self._voter_id in voter_id_list):
            self._voter_id = rd.randrange(1000000000, 9999999999)
        voter_id_list.add(self._voter_id)

    def cast_vote(self,candidate):
        if(election_status == False):
            print("Dear user you cannot caste your vote now because the election has not started yet or it may have completed!")
            print("")
            return
        if(self._is_registered_for_election == False):
            print(f"Dear user since you have not registered for the election so you are unable to caste your vote!")
            print("")
            return
        if(self._voter_id in vote_casted):
            print("Dear voter you have voted earlier!")
            print("")
            return
        if (candidate._is_registered_for_election == False):
            print(f"Dear voter you cannot vote for candidate {candidate.name} bcz he did not registered for the election!")
            print("")
            return
        print("vote polled successfully!")
        candidate._vote_count = candidate._vote_count + 1
        candidate_votes[candidate] = candidate._vote_count
        candidate._voted_history.append(f"Dear candidate you have earned a vote from {self.name}({self._voter_id})!")
        vote_casted.add(self._voter_id)
        print("")

    def view_profile(self):
        super().profile()
        print(f"Voter_id : {self._voter_id}")
        print("")

class Candidate(Person):
    def __init__(self,name : str,age : int,gender : str,party_name : str,party_symbol):
        super().__init__(name,age,gender)
        self._candidate_id = rd.randrange(1000,9999)
        self.party_name = party_name
        self.party_symbol = party_symbol
        while(self._candidate_id in candidate_id_list):
            self._candidate_id = rd.randrange(1000, 9999)
        self._is_registered_for_election = False
        candidate_id_list.add(self._candidate_id)
        self._vote_count = 0
        self._voted_history = []

    def view_profile(self):
        super().profile()
        print(f"Vote count : {self._vote_count}")
        print("")

    def vote_history(self):
        for i in self._voted_history:
            print(i)
        print("")

class Election:
    def __init__(self,election_name : str,year : int):
        self._election_name = election_name
        self._year = year
        self._voter_list = []
        self._candidate_list = []

    @staticmethod
    def set_election_status(status : bool):
        global election_status
        election_status = status
        if(election_status == False):
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(
                "--------------------------------- Election completed or it may have not started yet ------------------------------------------------")
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            return
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("--------------------------------- Election started successfully registered voters can proceed for voting! ------------------------------------------------")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------\n")


    @staticmethod
    def is_eligible_for_vote(age):
        if(age >= 18):
            return True
        return False

    def register_candidate(self,candidate):
        if(Election.is_eligible_for_vote(candidate.age) == False):
            print(f"Dear candidate you are not eligible for the election!")
            return
        print(f"Dear candidate your registration for {self._year} election has been recorded!")
        self._candidate_list.append(f"{candidate.name}({candidate._candidate_id} {candidate.party_name} {candidate.party_symbol})")
        candidate._is_registered_for_election = True
        print("")

    def register_voter(self,voter):
        print(f"Dear voter your registration for {self._year} election has been recorded!")
        self._voter_list.append(f"{voter.name}({voter._voter_id})")
        voter._is_registered_for_election = True
        print("")

    def voter_list_display(self):
        for i in self._voter_list:
            print(i)

    def winner(self):
        global votes
        winner = None
        max_votes = -1
        if(len(candidate_votes) == 0):
            print("Winner cannot decide because no one has ever voted!")
            print("")
            return
        for candidate in candidate_votes.keys():
            if(candidate._vote_count > max_votes):
                winner = candidate
                max_votes = candidate._vote_count

        draw_count = 0
        for candidate in candidate_votes.keys():
            if(max_votes == candidate._vote_count):
                draw_count = draw_count + 1

        if(draw_count > 1):
            print("The election has a draw!")
            return

        print(f"The {self._year} election winner is {winner.name} {winner.party_name} {winner.party_symbol}")
        print("")

candidate_1 = Candidate("Narendra Modi",75,"Male","BJP","🪷")

candidate_2 = Candidate("Rahul Gandhi",60,"Male","INC","✋")

person_1 = Voter("Sriram",45,"Male")

person_2 = Voter("Dheeraj",23,"Male")

person_3 = Voter("Thiru",56,"Male")

person_4 = Voter("Karthik",23,"Male")


election = Election("Main Elections",2026)


election.register_voter(person_1)

election.register_voter(person_2)

election.register_voter(person_3)

election.register_voter(person_4)


election.register_candidate(candidate_2)

election.register_candidate(candidate_1)


Election.set_election_status(True)


person_1.cast_vote(candidate_1)

person_2.cast_vote(candidate_1)

person_3.cast_vote(candidate_2)

person_4.cast_vote(candidate_2)


election.set_election_status(False)


candidate_1.vote_history()

candidate_2.vote_history()

election.winner()