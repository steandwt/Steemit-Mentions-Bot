from steem import Steem
from steem.blockchain import Blockchain
from steem.post import Post

#crate steem instance and pass it your key
s = Steem(keys = ["<your private posting key>"])
#create blockchain instance
b = Blockchain()

#stream the blockchain, map it to a Post object to make life easier and filter 
#them by comment since all comments and posts are of type: comment
stream = map(Post, b.stream(filter_by=['comment']))
#go through all the posts in the block
for post in stream:
    try:
        #get all the users tagged in the post
        users = post.json_metadata.get('users', [])
        #check if we are tagged
        if "<your-steemit-username-in-lowercase>" in users:
            #if we are tagged we'll upvote the post/comment with 10% voteweight. You
            #can change the vote accordingly
            post.vote(10.0, "<your steemit username>")

        else:
            #we are not tagged so we'll skip this post
            pass
        
        #Catch any unexpected exceptions
    except Exception as e:
        print("Error: "+str(e))
