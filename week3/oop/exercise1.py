class Books:
    print("Who wrote this")
    index = "Author-book"

    def hand_list(self, philosopher, book):
        print(Books.index)
        return f"{philosopher} wrote {book}"

whodunnit = Books()
print(whodunnit.hand_list("Sun Tzu", "The Art of War"))