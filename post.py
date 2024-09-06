class Post:
    postId = 0
    def __init__(self, author, title, description, image, publishedAt, content, url, id=None):
        self.title = title
        self.author = author
        self.description = description
        self.image = image
        self.publishedAt = publishedAt
        self.url = url
        self.content = content
        if self.content == None:
            id = Post.postId
            self.id = id
        else:
            Post.postId += 1
            id = Post.postId
            self.id = id


#function for password validation.
# --> remember to make sure you raise your custom errors

def validation(username, password):
    lowercase = [chr(i) for i in range(97, 123)]
    uppercase = [chr(j) for j in range(65, 91)]
    alphabets = lowercase + uppercase
    special_characters = ["1","2","3","4","5","6","7","8","9","0","!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", "-",
                          ".", "/", "=","{", "}", "[", "]", ",", ":", ";", "<", ">", "?", "@", "`", "~", "_", "|", "^"]
    
    has_upper = any(i in uppercase for i in password)
    has_lower = any(i in lowercase for i in password)
    has_char = any(i in special_characters for i in password)
    
    #check for username
    #maxlength handled in html file
    if not all(i in alphabets for i in username):
        return "Username can only contain alphabets"
    
    #check for password
    #max length handled in html file
    # Check for password containing at least one uppercase, one lowercase, and one special character
    if has_char and has_lower and has_upper:
        return True
    else:
        return ("Password must contain at least one uppercase letter, one lowercase letter, and one special character.")
