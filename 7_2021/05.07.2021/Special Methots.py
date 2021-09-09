class Movie:
    def __init__(self,title,directer,duration):
        self.title = title
        self.director  = directer
        self.duration = duration


    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Film Silindi")


m = Movie("Django","Tarantino",160)
print(m)

print(len(m))

del m 
print(m)
