# Heroku Test Repository

## Purpose

This repository is used to test Heroku and port existing projects to this platform. The goal is to support Herko as a demonstration platform in future repositories with simple small steps. The commits in the repository are not written according to the usual rules - please forgive me ;)

Once the repository reaches a clean state, the steps are combined into a proper README. So far, however, it's been more like trying, making mistakes, and correcting mistakes.

## Mission
The following steps and insights are to be achieved through this repository:

1. modify an existing repository without Heroku integration so that it can be run under Heroku
1.1 The repository consists of a docker container with a cron job to be executed and a website
1.2 The container is currently running permanently and should ideally only run at the time of the cron job (initiated by cron or similar) and the display of the website (initiated by user)
2. learn the necessary commands for this implementation
3. testing the behaviour and possibilities of Heroku
4. converting the original repository to Heroku support, without losing the previous startup and execution options
5. documentation of the necessary steps to be taken in order to be able to offer a recommendation for later changes in projects

## License

MIT, do whatever you want with it ;)

