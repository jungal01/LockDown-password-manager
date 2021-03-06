# LockDown
This project is licensed under the GNU General Public License.

LockDown is a password manager that can both generate and store passwords. The generated passwords are designed to be safe against brute force and some dictionary attacks. There are 2 fundamental styles; one of random characters, and one that generates relatively easy to remember passwords, inspired by the [XKCD comic](https://xkcd.com/936/). Password storage will create website associations and have an optional username and email fields for easy tracking. LockDown is security minded, and as such, will never offer cloud based syncing. It is up to the user to manage how passwords are stored until LockDown properly handles password storage. Later versions will include both GUI and CLI.

# Notes
- <code>words.txt</code> is the unformatted version of <code>dictionary.txt</code>, and was skimmed from 2 online dictionaries. <code>dictionary.txt</code> had extra formatting done by hand to remove vulgar language and to remove 'words' like <code>aaa</code>. If the purpose you choose to use this for needs some extra words, it's suggested to avoid use of <code>words.txt</code> and instead add the necessary words to <code>dictionary.txt</code>.
- At some point for speed and security, this project will be rewritten in Rust. The python version will remain available, however.
