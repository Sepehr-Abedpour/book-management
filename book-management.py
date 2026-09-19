# bakhsh 1 = list ketab ha 
books = [
    {
        'name':'kar az kar gozasht',
        'author':'sartr',
        'price':250
    },
    {
        'name':'boof kour',
        'author':'sadegh hedayat',
        'price':220
    },
    {
        'name':'aame pasand',
        'author':'bokofski',
        'price':275
    }
]

#bakhsh 2 = namayesh ketab ha
def show_books() :
    for i in range(len(books)) :
        print(
            i + 1,
            books[i]['name'],
            '|',
            books[i]['author'],
            '|',
            books[i]['price']
            
        )
        
#bakhsh 3 = ezafe kardan ketab
def add_book() :
    name = input('book name?')
    author = input('author?')
    price = int(input('price:'))
    
    book = {
        'name':name,
        'author':author,
        'price':price
    }
    books.append(book)
    print('book aded.')
    
# bakhsh 4 = hazf ketab
def remove_book() :
    show_books()
    number = int(input('enter book number :'))
    if 1 <= number <= len(books) :
        books.pop(number - 1)
        print('book removed.')
    else :
        print('invalid number.')
        
#bakhsh 5 = menu 
while True :
    print('\n===== library =====')
    
    print('1. show books')
    print('2. add book')
    print('3. remove book')
    print('4. exit')
    
    choice = input('choose:')
    if choice == '1':
        show_books()
    elif choice == '2':
        add_book()
    elif choice == '3':
        remove_book()
    elif choice =='4':
        break
    else :
        print('invalid choice.')
        
    
    
    