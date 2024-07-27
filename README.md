# how

An AI-based CLI assistant to help you with command line & shell.

## Demo 
Would be adding install instructions and better demo soon, until then check this out.
### Setup
![image](https://github.com/user-attachments/assets/87d3ba64-ecb7-43c6-9863-a62c39396ac5)

### Inferences
![image](https://github.com/user-attachments/assets/7af58310-183a-429b-aa66-e6abe36713fb)
![image](https://github.com/user-attachments/assets/20062ac2-1057-4139-9f60-990bd41605da)

## Usage

```console
$ how [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-v, --version`: Shows the version of the application
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `setup`: Sets up the configuration required to run...
* `to`: Sends the task to the LLM for analysis.

## `how setup`

Sets up the configuration required to run the application.
Set the LLM Provider & the corresponding API Key.

**Usage**:

```console
$ how setup [OPTIONS]
```

**Options**:

* `--interactive / --no-interactive`: Whether to use interactive mode for setting up configuration?  [default: interactive]
* `--provider TEXT`: The LLM Provider, needs to be passed explicitly if using --no-interactive mode.
* `--api-key TEXT`: The API Key for the LLM provider, needs to be passed explicitly if using --no-interactive mode.
* `--help`: Show this message and exit.

## `how to`

Sends the task to the LLM for analysis.
Returns the commands to be executed in order to achieve that.

**Usage**:

```console
$ how to [OPTIONS] TASK
```

**Arguments**:

* `TASK`: The command line task to perform.  [required]

**Options**:

* `--help`: Show this message and exit.

