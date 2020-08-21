# Heroku Test Repository

## Purpose

This repository is used to test Heroku and port existing projects to this platform. The goal is to support Herko as a demonstration platform in future repositories with simple small steps. The commits in the repository are not written according to the usual rules - please forgive me ;)

Once the repository reaches a clean state, the steps are combined into a proper README. So far, however, it's been more like trying, making mistakes, and correcting mistakes.

## Mission
The following steps and insights are to be achieved through this repository:

1. Modify an existing repository without Heroku integration so that it can be run under Heroku
1.1 The repository consists of a docker container with a cron job to be executed and a website
1.2 The container is currently running permanently and should ideally only run at the time of the cron job (initiated by cron or similar) and the display of the website (initiated by user)
2. Learn the necessary commands for this implementation
3. Testing the behaviour and possibilities of Heroku
4. Converting the original repository to Heroku support, without losing the previous startup and execution options
5. Documentation of the necessary steps to be taken in order to be able to offer a recommendation for later changes in projects

## Sources

This repository is based on the original repository [fah-red-lions-backend](https://github.com/generaliinformatik/fah-red-lions).

## Test it

You are welcome to test this repository yourself. Feel free to use the button below or integrate your own repository into Heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Status achieved (will be updated)

- [OK] Integrate repository or components  
- [OK] allow basic access to the website (without data)  
- [OK] Display the website as original (without data)  
- [OK] Displays the first data in Web page  
- [--] Regular data retrieval and storage in containers  
- [--] Conversion of the original repository to Heroku support

## License

MIT, do whatever you want with it ;)

