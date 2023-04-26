from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, father, brother, cousin, grandson, descendant')
+father('a', 'b')
+father('a', 'c')
+father('b', 'd')
+father('b', 'e')
+father('c', 'f')
brother(X,Y) <= father(Z,X) & father(Z,Y)
cousin(X,Y) <= brother(X,Z) & brother(Y,Z)
grandson(X,Y) <= father(Y,Z) & father(Z,X)
descendant(X, Y) <= father(Y, X)
descendant(X, Y) <= father(Z, X) & descendant(Z, Y)
print(f"brother(X,Y): {pyDatalog.ask('brother(X,Y)')}")
print(f"cousin(X,Y): {pyDatalog.ask('cousin(X,Y)')}")
print(f"grandson(X,Y): {pyDatalog.ask('grandson(X,Y)')}")
print(f"descendant(X,Y): {pyDatalog.ask('descendant(X,Y)')}")




from pyDatalog import pyDatalog
pyDatalog.create_terms('big, small, grey, black, brown, dark')
dark(X) <= brown(X)
dark(X) <= black(X)
+big('bear')
+big('elephant')
+small('cat')
+brown('bear')
+black('cat')
+grey('elephant')
print(pyDatalog.ask('dark(X) & big(X)'))



from pyDatalog import pyDatalog

pyDatalog.create_terms('marks, passm')

marks['Ram'] = 90
marks['Raju'] = 45
marks['Priya'] = 85
marks['Carol'] = 70
marks['Shyam'] = 80

print(pyDatalog.ask('marks[X] == Y'))
print(pyDatalog.ask('marks[X] == 80'))
print(pyDatalog.ask('marks["Priya"] == Y'))

passm(X) <= (marks[X] >= 60)
print(pyDatalog.ask('passm(X)'))




marks = {
    'Ram': 90,
    'Raju': 45,
    'Priya': 85,
    'Carol': 70,
    'Shyam': 80
}
for name, mark in marks.items():
    print(f"{name}: {mark}")
for name, mark in marks.items():
    if mark == 80:
        print(name)
for name, mark in marks.items():
    if name == 'Priya':
        print(mark)
for name, mark in marks.items():
    if mark >= 60:
        print(name)
        
        
        

from pyDatalog import pyDatalog 
pyDatalog.create_terms('factorial, N')   
factorial[N] = N * factorial[N-1]  
factorial[1] = 1   
print(pyDatalog.ask('factorial[5] == X'))




from pyDatalog import pyDatalog
pyDatalog.create_terms('A, B, male, female, parent, husband, wife, father, mother, brother, sister, cousin, grandmother, uncle, aunt, grandfather')
+parent('mike', 'lennard')
+parent('mike', 'lena')
+parent('lennard', 'donald')
+parent('lennard', 'hillary')
+parent('lennard', 'usain')
+parent('lena', 'adam')
+parent('lena', 'simon')
+parent('donald', 'lisa')
+parent('hillary', 'joar')
+parent('hillary', 'elise')
+male('mike')
+male('lennard')
+female('lena')
+male('donald')
+female('hillary')
+female('usain')
+male('adam')
+female('simon')
+female('lisa')
+male('joar')
+female('elise')
+male('dan')
father(X, Y) <= parent(X, Y) & male(X)
mother(X, Y) <= parent(X, Y) & female(X)
wife(X, Y) <= female(X) & male(Y) & (parent(X, Z) & parent(Y, Z))
husband(X, Y) <= male(X) & female(Y) & (parent(X, Z) & parent(Y, Z))
father(X, Y) <= male(X) & parent(X, Y)
mother(X, Y) <= female(X) & parent(X, Y)
sister(X, Y) <= female(X) & parent(Z, X) & parent(Z, Y) & (X != Y)
brother(X, Y) <= male(X) & parent(Z, X) & parent(Z, Y) & (X != Y)
grandmother(X, Y) <= female(X) & parent(X, Z) & parent(Z, Y)
grandfather(X, Y) <= male(X) & parent(X, Z) & parent(Z, Y)
cousin(X, Y) <= parent(A, X) & parent(B, Y) & (A != B) & brother(A, B)
cousin(X, Y) <= parent(A, X) & parent(B, Y) & (A != B) & sister(A, B)
uncle(X, Y) <= male(X) & (sister(B, A) & husband(X, B)) & parent(A, Y)
uncle(X, Y) <= male(X) & (sister(B, A) & husband(X, B)) & parent(A, Y)
aunt(X, Y) <= female(X) & sister(X, A) & parent(A, Y)
aunt(X, Y) <= female(X) & (brother(B, A) & wife(X, B)) & parent(A, Y)
print(pyDatalog.ask('cousin(X, "adam")'))
print(pyDatalog.ask('grandfather(X, "elise")'))




from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, A, B, male, female, parent, father, mother, husband, sister, brother, grandmother, grandfather, ancestor, cousin, uncle, son, daughter, children')
+parent('Dicky', 'Oliver')
+parent('Dicky', 'Sophie')
+parent('Oliver', 'Anne')
+parent('Oliver', 'Mike')
+parent('Oliver', 'Jack')
+parent('Sophie', 'Rose')
+parent('Rose', 'George')
+male('Dicky')
+male('Oliver')
+female('Sophie')
+female('Anne')
+male('Mike')
+male('Jack')
+female('Rose')
+male('George')
father(X, Y) <= parent(X, Y) & male(X)
mother(X, Y) <= parent(X, Y) & female(X)
husband(X, Y) <= male(X) & female(Y) & (parent(X, Z) & parent(Y, Z))
father(X, Y) <= male(X) & parent(X, Y)
mother(X, Y) <= female(X) & parent(X, Y)
brother(X, Y) <= father(Z, X) & father(Z, Y) & male(X)
sister(X, Y) <= father(Z, X) & father(Z, Y) & female(X)
grandmother(X, Y) <= female(X) & parent(X, Z) & parent(Z, Y)
grandfather(X, Y) <= male(X) & parent(X, Z) & parent(Z, Y)
cousin(X, Y) <= parent(A, X) & parent(B, Y) & (A != B) & brother(A, B)
cousin(X, Y) <= parent(A, X) & parent(B, Y) & (A != B) & sister(A, B)
uncle(X, Y) <= male(X) & (sister(B, A) & husband(X, B)) & parent(A, Y)
uncle(X, Y) <= male(X) & (sister(B, A) & husband(X, B)) & parent(A, Y)
ancestor(X, Y) <= parent(X, Y)
ancestor(X, Y) <= parent(A, Y) & ancestor(X, A)
son(X, Y) <= male(X) & parent(Y, X)
daughter(X, Y) <= female(X) & parent(Y, X)
children(X, Y) <= son(X, Y)
children(X, Y) <= daughter(X, Y)
print(pyDatalog.ask('parent("Oliver", "George")'))
print(pyDatalog.ask('parent(X, "Oliver")'))
print(pyDatalog.ask('children(X, "Oliver")'))
print(pyDatalog.ask('brother(X, "Anne")'))
print(pyDatalog.ask('cousin(X, "Rose")'))