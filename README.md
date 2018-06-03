# passwordGenerator
This project is licensed under the GNU General Public License.

This generator creates a password of various lengths, with a minimum of 8 characters, and a maximum of 30 characters. This is designed to create random passwords invulnerable to brute force and dictionary attacks. This program will never repeat a password either. There are 2 fundemental styles, one of random characters, and one that generates relatively easy to remember xkcd-style passwords, found [here](https://xkcd.com/936/). This current version creates cryptographically random passwords, but gets hashed and stored in an unprotected file. It is up to the user to manage how passwords are stored, however there is a dependance upon the file holding generated passwords. Later versions will incude a GUI.

# Notes
- <code>words.txt</code> is the unformatted version of <code>dictionary.txt</code>, and was skimmed from 2 online dictionaries. <code>dictionary.txt</code> had extra formatting done by hand to remove vulgar language and to remove 'words' like <code>aaa</code>. If the purpose you choose to use this for needs some extra words, it's suggested to avoid use of <code>words.txt</code> and instead add the necessary words to <code>dictionary.txt</code>.
- Password Generator is transitioning to a fully fledged password manager. A name change is in the works.
- Due to some illuminating courses I took on information security, the passwords will no longer stored in any form until I figure out securely encrypting entire files. Instead, this old feature will be modified to be a fully featured password cracker.
- At some point for speed and security, this project will be rewritten in Rust. The python version will remain available, however.

# Todo
- [ ] create a CLI
- [ ] implement urandom instead of systemrandom
- [ ] implement string module
- [ ] allow for percentage of leet
- [ ] store and encrypt passwords with AES 256
- [ ] allow user passwords to be entered
- [ ] create a GUI
- [ ] allow user to choose a single password or combine words from generated list

