

import random
import string


class Codec:
    my_dictionary = {}
    def random_code(self):
         chars = string.ascii_letters + string.digits
         random_code_generator = "".join(random.choice(chars) for _ in range(6))
         return random_code_generator
     

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        my_url = "http://tinyurl.com/"
        
        my_random_code = self.random_code()
        while my_random_code in self.my_dictionary:
            my_random_code = self.random_code()
        self.my_dictionary[my_random_code] = longUrl
        
        return  my_url+my_random_code
 

    def decode(self, shortUrl: str) -> str:
        my_url = "http://tinyurl.com/"

        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.replace(my_url, "")
        
        return self.my_dictionary.get(code)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

url = "https://leetcode.com/problems/design-tinyurl"
c1 = Codec()
result = c1.decode(c1.encode(url))
print(result)
