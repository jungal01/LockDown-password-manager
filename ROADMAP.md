# Road Map for LockDown

  LockDown has several goals and ideas. With several goals potentially comes several bugs, so to keep track of all three, we keep them here.

## How to Read This File

  The [issues being fixed](#issues-being-fixed) section is for issues being actively worked on.

  The [known issues](#known-issues) section is for issues that have been identified by the team, or have verified the issue exists by the team through the issue tracker.

  The [potential issues](#potential-issues) section is for issues that have either been identified as a potential issue, or have been acknowledged from the issue tracker. No issues in this section have been verified.

  The [new features](#new-features) section are for features that don't exist yet, but will be added.

  The [improving features](#improving-features) section is for adding additional usage to features that currently exist.

  The [core functionality](#core-functionality) section is for features that are required to have a fully functioning password manager.

  The [core improvements](#core-improvements) section is for necessary changes to the core features, that may or my not break compatibility.

  The [miscellaneous](#miscellaneous) section is for all aspects of the project that do not strictly fit the other categories.

## Issues Being Fixed

## Known Issues

  * password generation is slow (python limitations)

## Potential Issues

* The CLI may not be compatible with Windows based systems

## New Features

- [ ] Graphical User Interface
- [ ] Allow multiple users
- [ ] Store passwords through Command Line Interface (cli): 2020-02-20
- [ ] Allow user to choose a single password or combine words from generated list
- [ ] username/password data breach query to haveibeenpwned.com
- [ ] iOS app
- [ ] Android app


## Improving Features

## Core Functionality

 - [x] Create CLI
 - [x] Create Password Generator
 - [x] Create RSA library
 - [x] Create AES library
 - [ ] Create AES-RSA hybrid library
 - [ ] Design password file format
 - [ ] Store password/account details
 - [ ] Authenticate user(s)

 ## Core Improvements

 - [ ] Allow for percentage of leet in PasswordGenerator
 - [ ] Implement string module for PasswordGenerator
 - [ ] Implement secrets instead of systemrandom in PasswordGenerator
 - [ ] Add other encryption methods i.e. salsa20, ChaCha20, Blowfish


## Miscellaneous

  * Design a logo
  * Windows Installation Wizard
  * Tarball on github pages
  * dedicated website
