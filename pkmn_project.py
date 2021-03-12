class Pokemon:
    def __init__(self, name, type1, type2=None, levitate=False):
        type1 = type1.lower()
        supereffective = []
        notvery = []
        immunity = []
        types = [type1]
        if type2 is not None:
            type2 = type2.lower()
            types.append(type2)
        if levitate is not False:
            immunity.append("ground")
        weaknesses = {
            "normal" : ["fighting"],
            "fire" : ["water", "ground", "rock",],
            "water" : ["electric", "grass"],
            "electric" : ["ground"],
            "grass" : ["fire", "ice", "poison", "flying", "bug"],
            "ice" : ["fire", "fighting", "rock", "steel"],
            "fighting" : ["flying", "psychic", "fairy"],
            "poison" : ["ground", "psychic"],
            "ground" : ["water", "grass", "ice"],
            "flying" : ["electric", "ice", "rock"],
            "psychic" : ["bug", "ghost", "dark"],
            "bug" : ["fire", "flying", "rock"],
            "rock": ["water", "grass", "fighting", "ground", "steel"],
            "ghost" : ["ghost", "dark"],
            "dragon" : ["ice", "dark"],
            "dark" : ["fighting", "bug", "fairy"],
            "steel" : ["fire", "fighting"],
            "fairy" : ["poison", "steel"]
        }
        resistances = {
            "normal" : [],
            "fire" : ["fire", "grass", "ice", "bug", "steel", "fairy"],
            "water" : ["fire", "water", "ice", "steel"],
            "electric" : ["electric", "flying", "steel"],
            "grass" : ["water", "electric", "grass", "ground"],
            "ice" : ["ice"],
            "fighting" : ["bug", "rock", "dark"],
            "poison" : ["grass", "fighting", "poison", "bug", "fairy"],
            "ground" : ["poison", "rock"],
            "flying" : ["grass", "fighting", "bug"],
            "psychic" : ["fighting", "psychic"],
            "bug" : ["grass", "ground", "fighting"],
            "rock" : ["normal", "fire", "poison", "flying"],
            "ghost" : ["poison", "bug"],
            "dragon" : ["fire", "water", "electric", "grass"],
            "dark" : ["ghost", "dark"],
            "steel" : ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"],
            "fairy" : ["fighting", "bug", "dark"]
        }
        notaffect = {
            "normal" : ["ghost"],
            "ground" : ["electric"],
            "flying" : ["ground"],
            "ghost" : ["fighting", "normal"],
            "dark" : ["psychic"],
            "steel" : ["poison"],
            "fairy" : ["dragon"]
        }
        for i in types:
            w = weaknesses.get(i)
            r = resistances.get(i)
            n = notaffect.get(i)
            if w is not None:
                supereffective.extend(w)
            else:
                raise TypeError("Not a valid Pokemon Type given.")
            if r is not None:
                notvery.extend(r)
            else:
                raise TypeError("Not a valid Pokemon Type given.")
            if n is not None:
                immunity.extend(n)
        for i in notvery:
            count = 0
            for j in notvery:
                if i == j:
                    count += 1
                if count == 2:
                    temp = i + " (1/4x)"
                    notvery.remove(i)
                    notvery.remove(j)
                    notvery.append(temp)
                    break
        for i in supereffective:
            count = 0
            for j in supereffective:
                if i == j:
                    count += 1
                if count == 2:
                    temp = i + " (4x)"
                    supereffective.remove(i)
                    supereffective.remove(j)
                    supereffective.append(temp)
                    break

        for i in immunity:
            for j in notvery:
                if i == j:
                    notvery.remove(j)
            for j in supereffective:
                if i == j:
                    supereffective.remove(j)
        self.name = name
        self.type1 = type1[0].upper() + type1[1:]
        if type2 is not None:
            self.type2 = type2[0].upper() + type2[1:]
        else:
            self.type2 = None
        self.immunities = self.__fixCase(immunity)
        self.supereffective = self.__fixCase(supereffective)
        self.resistances = self.__fixCase(notvery)
    def __fixCase(self, x):
        for i in range(0, len(x)):
            uppercase = x[i]
            x[i] = uppercase[0].upper() + uppercase[1:]
        return x        
    def __str__(self):
        retString = ""
        dashes = ["-" for i in range(0, 75)]
        dashes = "".join(dashes)
        s_length = len(self.supereffective)
        r_length = len(self.resistances)
        i_length = len(self.immunities)
        length = 0
        if s_length >= r_length:
            length = s_length
        elif r_length >= i_length:
            length = r_length
        else:
            length = i_length
        if length == 1:
            length += 1

        if self.type2 == None:
            retString += "{:} ({:})\n".format(self.name, self.type1)
            retString += dashes
            retString += "\n"
            retString += "{:^25}{:^25}{:^25}\n".format("Weaknesses", "Resistances", "Immunities")
        else:
            retString += "{:} ({:} & {:})\n".format(self.name, self.type1, self.type2)
            retString += dashes
            retString += "\n"
            retString += " {:^25}{:^25}{:^25}\n".format("Weaknesses", "Resistances", "Immunities")
        retString += dashes + "\n"
        for i in range(0, length - 1):
            try:
                retString += "{:^25}".format(self.supereffective[i])
            except:
                retString += "{:^25}".format("")
            try:
                retString += "{:^25}".format(self.resistances[i])
            except:
                retString += "{:^25}".format("")
            try:
                retString += "{:^25}".format(self.immunities[i])
            except:
                retString += "{:^25}".format("")

            retString += "\n"
        return retString
    def __lt__(self, other):
        return self.name < other.name