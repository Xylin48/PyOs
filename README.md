# PyOs

**A Python-built operating environment, application launcher, and central hub for personal projects and games.**

> Original project description: “a full operating system built in python made for hosting my projects and games a hub”

PyOs was designed around a deceptively ambitious idea: **instead of every project being a separate program with a separate starting point, give them a shared home.** The repository contains an interactive command interface, filesystem tools, a user-identity experiment, a prototype software store, a social application, games, utilities, and an early graphical interface.

The word **hub** is central to the project. PyOs is not simply a collection of scripts with a convenient folder name. Its design points toward a single environment from which users can discover, launch, manage, and eventually connect many different applications. Some of those connections are implemented in the archived source; others are early prototypes or ideas recorded in comments.

**Historical/technical clarification:** The original author describes PyOs as a “full operating system.” In the surviving source, it is more precisely a **Python-based OS-like environment running on top of an existing host OS**, using host shell commands, Replit services, and external programs. The archive does not contain an independent bootloader, kernel, hardware drivers, or a complete standalone operating system. This distinction does not diminish the scope of its intended application ecosystem.

## Contents

1. [The vision: what “a hub” means](#the-vision-what-a-hub-means)
2. [How the pieces fit together](#how-the-pieces-fit-together)
3. [Repository map](#repository-map)
4. [The command interface](#the-command-interface)
5. [The Store and application distribution](#the-store-and-application-distribution)
6. [Identity and persistent data](#identity-and-persistent-data)
7. [Social and the Book experiment](#social-and-the-book-experiment)
8. [Games and entertainment](#games-and-entertainment)
9. [Utilities and graphical experiments](#utilities-and-graphical-experiments)
10. [Execution model and dependencies](#execution-model-and-dependencies)
11. [Current state and limitations](#current-state-and-limitations)
12. [Project history and design significance](#project-history-and-design-significance)
13. [Source reference index](#source-reference-index)

## The vision: what “a hub” means

PyOs was intended to be the **place where the author's other projects live**. This is a different goal from writing one game, one calculator, or one social application. A hub has to provide an environment around those programs.

### 1. One entry point for different experiences

A user should be able to enter PyOs and choose what to do next: inspect files, run a program, open a game, use a utility, or visit a social application. The central command interpreter in [`Home/com.py`](Home/com.py) is the clearest surviving expression of that idea. It accepts multiple named commands and dispatches to other files or host utilities.

The important architectural idea is **centralized navigation**: individual programs do not need to be the user's entire experience. They can be destinations within a larger one.

### 2. A common home for projects

The repository separates [`Apps/`](Apps/), [`Home/`](Home/), [`Home/Games/`](Home/Games/), and [`gui/`](gui/). These are not yet a formal package-management standard, but the arrangement shows an intended division between the environment itself, applications, games, and interface experiments.

The shell's `run` command can execute a chosen Python file, while `games` invokes a shell script. These mechanisms illustrate the hub's role as a **launcher and organizer**, even though they are not yet a unified application API.

### 3. A place to acquire new software

[`Apps/store.py`](Apps/store.py) is the most explicit example of the hub becoming an **expandable ecosystem**. The Store offers Cookie and attempts to clone its Git repository into `./Home/Games/Cookie`.

That means the concept was not limited to programs already bundled with PyOs. The design was beginning to support a workflow of:

1. Enter the shared environment.
2. Select software in a store.
3. Retrieve that software from an external repository.
4. Place it inside the hub's organized application/game space.
5. Eventually make it available as part of the same environment.

**Only the selection and Git-clone portion is represented in the archived Store prototype.** Automatic registration, launch integration, dependency management, uninstalling, update tracking, and permissions are not implemented there.

### 4. Identity across the environment

[`Home/usr.py`](Home/usr.py) writes a user's name to Replit's database, and [`Home/com.py`](Home/com.py) has a `whoami` command that combines the Replit owner with the saved name. [`Home/social.py`](Home/social.py) separately experiments with usernames and passwords.

These are rudimentary and not yet a consistent account system. But their presence matters: the hub was being conceived as a place **inhabited by a user**, not just a static menu of files.

### 5. More than a terminal

[`gui/guitest.py`](gui/guitest.py) creates a Tkinter window with “Login Screen” and “Boot Screen” labels and displays [`gui/load.gif`](gui/load.gif). It is a small experiment, not a complete desktop, but it demonstrates that PyOs's envisioned environment was not necessarily confined to text.

### 6. Connected projects, not isolated demos

The strongest evidence for the “hub” interpretation is the combination of these systems: a command shell, a file layout, user identity, a Store, a social program, games, and a GUI experiment. Each could have been a standalone exercise; PyOs groups them around the idea of **one place to access many experiences**.

This is an interpretation of the design supported by the code and the author's stated purpose—not a claim that every integration was finished.

## How the pieces fit together

```text
                        PyOs
          Python-based central environment
                          |
                Home/main.py
                configured entry point
                          |
                  Home/com.py
             interactive command shell
                   /      |       \
                  /       |        \
         File / host    Launcher    User identity
          commands      commands      + Replit DB
                            |
             +--------------+----------------+
             |              |                |
          Apps/          Home/Games/       Home/social.py
       calculator,       Tic-Tac-Toe,      accounts, posts,
       Store prototype   Cookie concept    user search
             |              |
          Store ---- Git clone into Games/
             |
       external repositories

        gui/guitest.py: separate GUI experiment
        Home/book.py: separate social/Book experiment
```

**Important:** This is a conceptual architecture diagram, not a verified end-to-end runtime call graph. The archived `Home/main.py` currently contains an invalid import statement, and several components are not wired together cleanly.

## Repository map

| Path | Role | Status in archived source |
| --- | --- | --- |
| [`Home/main.py`](Home/main.py) | Configured Python entry point | Very small; contains startup errors |
| [`Home/com.py`](Home/com.py) | Main command interpreter and host command bridge | Substantial prototype |
| [`Home/usr.py`](Home/usr.py) | Create/store a display name | Basic implementation |
| [`Home/social.py`](Home/social.py) | Text-based social environment | Alpha prototype |
| [`Home/book.py`](Home/book.py) | Early Book feature | Placeholder |
| [`Apps/store.py`](Apps/store.py) | Software discovery/download prototype | One listed application |
| [`Apps/calc.py`](Apps/calc.py) | Expression calculator | Small working concept, unsafe evaluation |
| [`Home/Games/test.sh`](Home/Games/test.sh) | Tic-Tac-Toe in Bash | Playable game logic |
| [`Home/Games/firefox.sh`](Home/Games/firefox.sh) | Browser launcher experiment | Host command stub |
| [`Home/Games/game.sh`](Home/Games/game.sh) | Game-related placeholder | Empty |
| [`Cookie/`](Cookie/) | Archived Cookie Clicker-style game | Separate substantial project |
| [`gui/guitest.py`](gui/guitest.py) | Tkinter interface experiment | Prototype |
| [`gui/load.gif`](gui/load.gif) | GUI loading asset | Asset |
| [`Updates.md`](Updates.md) | Original change notes | Historical record |
| [`.replit`](.replit) | Replit execution configuration | Historical configuration |
| [`pyproject.toml`](pyproject.toml) | Poetry package metadata | Historical dependencies |
| [`replit.nix`](replit.nix) | Replit/Nix dependency specification | Historical environment |

The repository is a **source archive**. Some historical binary/dependency files may not be present in the GitHub copy; the original PyOs ZIP is the most complete preserved snapshot.

## The command interface

**Primary reference:** [`Home/com.py`](Home/com.py)

The command interface is the heart of the PyOs environment. It repeatedly displays a text logo, prompts with `>>>`, reads a command, and selects behavior using a series of conditional statements.

### Filesystem commands

| Command | Intended action |
| --- | --- |
| `mkdir` | Create a directory |
| `mkfile`, `touch` | Create a file |
| `rmdir` | Remove a directory |
| `rmfile` | Remove a file |
| `dir`, `ls` | List files |
| `cat` | Display a file |
| `edit` | Attempt to open a file in Vim |
| `cd` | Attempt to change directory |
| `clear` | Clear the terminal |

Most commands call the host system via `os.system(...)`. Consequently, PyOs is acting as an **interface to the underlying operating system**, not implementing its own filesystem.

There are implementation details worth preserving in the documentation: `cd` runs in a subprocess and therefore does not persistently change Python's current directory; the `edit` command includes a literal `$vim` string; and unescaped user input is concatenated into shell commands. These are limitations of the original code, not recommended patterns for a new implementation.

### Environment and system commands

| Command | Intended action |
| --- | --- |
| `whoami` | Show Replit owner and saved display name |
| `ip` | Run `hostname -I` |
| `echo` | Print entered text |
| `bash` | Invoke a shell script |
| `reboot` | Attempt host reboot |
| `internet speed` | Clone/run an external speed-test project |
| `help` | Display a short command list |
| `quit` | Exit the program |

The shell also attempts `apt-get install wget` on each loop iteration. This is historical behavior, not an installation procedure users should reproduce.

### Application launch commands

| Command | Intended action |
| --- | --- |
| `mkusr` | Execute the user setup script |
| `firefox` | Invoke the Firefox launcher shell script |
| `games` | Invoke the game script |
| `run` | Execute a user-selected Python file |

The `run` implementation uses `exec(open(path).read())`, demonstrating a general-purpose launcher concept, but it also means the chosen file executes with the process's privileges. It is **not a sandbox**.

The shell currently has no formal plugin registry, command routing table, process manager, or security boundary. Its significance is the breadth of behavior gathered behind one prompt.

## The Store and application distribution

**Primary reference:** [`Apps/store.py`](Apps/store.py)

The Store is one of PyOs's most important architectural prototypes because it turns the hub from a fixed collection of programs into something that could grow.

The surviving implementation:

- Prints `Welcome to The Store` and `Not much to do here`.
- Presents **Cookie** as an available selection.
- Defines a Git repository URL for the Cookie project.
- Targets `./Home/Games/Cookie` as the installation directory.
- Attempts `git clone` and prints a success or failure message based on the return code.

The code comments also mention an intention to download a **text-based social media** application and package it. This suggests that games were not the only envisioned category of downloadable software.

### Why the Store matters to the hub concept

A hub needs a way to bring in more content. The Store introduces a distinction between **the environment** (PyOs) and **software obtained for the environment** (Cookie and potentially Social). It is an early form of software distribution using Git repositories as the source of packages.

The design also establishes a meaningful destination: the application is placed inside the PyOs hierarchy rather than downloaded to an arbitrary location.

### Prototype limitations

The archived `store.py` uses `os.system` without importing `os` locally; it assumes that `os` is already available in its execution context. The Git URL references an older repository owner path, and there is no robust validation, rollback, installation manifest, or automatic launch hook. Treat this as an **original blueprint**, not a production-ready package manager.

## Identity and persistent data

**References:** [`Home/usr.py`](Home/usr.py), [`Home/com.py`](Home/com.py), [`Home/social.py`](Home/social.py)

PyOs uses **Replit DB** in several places. The user-setup script asks for a name and writes it to `db["name"]`. The command shell's `whoami` reads that value alongside the `REPL_OWNER` environment variable.

The Social experiment separately asks for a username and password and stores entries in the database. However, its conditional checks and assignments do not implement reliable authentication: it uses usernames and passwords as database keys, stores literal marker strings, and can overwrite values. The code also does not provide password hashing or secure session management.

The architectural theme is **persistent identity inside the hub**. The archived implementation is only a first step toward that goal.

## Social and the Book experiment

**References:** [`Home/social.py`](Home/social.py), [`Home/book.py`](Home/book.py)

Social is a terminal-based application with an account prompt and its own `>>>` loop. Its recognized commands include:

- `clear` — clear the screen.
- `book` — attempt to open the Book feature.
- `settings` — display an alpha-stage placeholder.
- `post` — accept a text post.
- `search` — check whether a username exists in the database.

The source explicitly warns that **posts do not get saved yet**. Its file-output handling is also incomplete: it prints a post, assigns the return value of `print` (which is `None`), then writes that value to a file while redirecting `sys.stdout`. This is not a functioning social feed or durable post store.

The Book script imports Social, prints a placeholder message and the username, then sleeps briefly. It is best understood as a **feature stub**.

### How Social supports the hub vision

Social changes the role of PyOs from a launcher of utilities to a potential **shared digital space**. The presence of usernames, searching, posting, and feature navigation implies that the environment could eventually host activities centered on people and information, not only executable programs.

## Games and entertainment

### Tic-Tac-Toe

**Reference:** [`Home/Games/test.sh`](Home/Games/test.sh)

The Bash Tic-Tac-Toe program is one of the more substantial finished pieces in the archive. It contains:

- A numbered 3×3 terminal board.
- Colored terminal output.
- One-player mode against a randomized bot.
- Local two-player mode with names.
- Turn selection and input handling.
- Win/draw detection and restart/menu flow.

Its comments identify development from **February 16–18, 2022**. This makes it an especially useful historical artifact: PyOs brought an earlier standalone game into a larger environment.

### Cookie

**References:** [`Cookie/cookie.py`](Cookie/cookie.py), [`Cookie/guide.py`](Cookie/guide.py), [`Cookie/news.py`](Cookie/news.py)

Cookie is a much larger terminal game built around clicking for cookies, purchasing upgrades, increasing production, receiving special rewards, saving progress, and displaying changing news headlines. It uses Replit DB for saved state and includes a sizeable upgrade catalog.

Its presence in the archive—and its separate mention in the Store—illustrates two complementary approaches to the hub: **bundled software** and **software that can be downloaded**.

Cookie has its own implementation quirks and historical dependencies. It should be understood as a separate game project housed within the PyOs archive, not as functionality implemented by the PyOs command interpreter itself.

### Firefox

**Reference:** [`Home/Games/firefox.sh`](Home/Games/firefox.sh)

The archive contains a minimal Firefox launcher stub. [`Updates.md`](Updates.md) also records Firefox as an upcoming feature. This points toward PyOs serving as an access point to **host applications** in addition to its own Python and Bash programs.

## Utilities and graphical experiments

### Calculator

**Reference:** [`Apps/calc.py`](Apps/calc.py)

The calculator prompts for an expression and evaluates it using Python's `eval`. This is a simple utility prototype. **Do not enter untrusted expressions:** `eval` can execute arbitrary Python code. A modern version should use a restricted mathematical parser instead.

### Tkinter GUI

**References:** [`gui/guitest.py`](gui/guitest.py), [`gui/load.gif`](gui/load.gif)

The GUI test creates a window titled `Tk Example`, sets its geometry, displays login/boot labels, and loads an animated-image asset through Tkinter's `PhotoImage`.

This is not yet a graphical PyOs shell, login manager, or desktop. Its significance is the attempt to give the environment a **visual entry point**, which complements the terminal-based architecture.

## Execution model and dependencies

PyOs was built around a historical **Replit + Python + Bash/Linux** environment.

The archive includes:

- [`.replit`](.replit): points the run command at `python3 ./Home/main.py`.
- [`pyproject.toml`](pyproject.toml): Poetry metadata with Python 3.8-era constraints and dependencies including `numpy` and `getkey`.
- [`replit.nix`](replit.nix): historical Replit/Nix dependencies, including Python packages, Firefox, and Wget.
- Several modules importing `replit.db`, which is not a standard Python library.
- Shell commands relying on Linux utilities and external executables.

### Historical startup path

The configured entry point is:

```bash
python3 ./Home/main.py
```

**This is documentation of the original configuration, not a verified working launch command.** In the archived file, `import com.py` is invalid Python syntax, and `db` is referenced without an import. The `.replit` configuration also uses a differently capitalized `entrypoint` path. The project will require repairs and environment setup to run reliably on a modern system.

### For developers examining the archive

1. Read `Home/com.py` to understand the main user-facing interaction model.
2. Read `Apps/store.py` to understand how external applications were intended to join the environment.
3. Read `Home/usr.py` and `Home/social.py` to understand identity and persistence experiments.
4. Read `Home/Games/test.sh` and `Cookie/` to see the kinds of software the hub was designed to host.
5. Read `gui/guitest.py` for the beginnings of a graphical interface.
6. Consult `Updates.md` and the configuration files for historical context.

Do not run the archive with elevated privileges or use its shell execution, authentication, or `eval` patterns in a trusted production environment without review.

## Current state and limitations

PyOs is preserved here as a **historical development project**, with ambitious architecture and multiple working concepts but incomplete integration.

| Area | What exists | What is not established |
| --- | --- | --- |
| Shell | Interactive command dispatch and host command execution | Independent OS services, secure shell, reliable startup |
| Store | Cookie selection and Git clone attempt | Full package lifecycle and automatic integration |
| Users | Replit DB name storage | Unified, secure authentication |
| Social | Account prompts, posting/search command prototypes | Reliable post persistence, secure accounts, full network |
| Games | Tic-Tac-Toe logic and Cookie source | Unified launcher for every game |
| GUI | Tkinter window and asset loading | Integrated graphical desktop |
| Persistence | Replit DB calls in multiple components | Portable, consistent storage abstraction |
| Platform | Replit/Python/Linux configuration | Standalone bootable OS |

Other known limitations include command execution by string concatenation, inconsistent working-directory assumptions, missing imports, incomplete error handling, platform-specific commands, and outdated dependency declarations.

These caveats are part of an accurate record of the code. They do not erase the architectural purpose: **PyOs was designed to unify programs into an expandable environment.**

## Project history and design significance

The archive contains multiple layers of development history.

- **February 16–18, 2022:** The Tic-Tac-Toe script's comments identify its original development period.
- **February 19, 2025:** [`Updates.md`](Updates.md) records Tic-Tac-Toe, user creation, command functionality, and plans for Firefox.
- **February 21, 2025:** The update notes record the import of social media code and a calculator.
- **Later preservation:** The original project was archived and published as a GitHub repository, retaining the experimental source rather than rewriting its history.

### The larger idea

The interesting part of PyOs is not whether its command interpreter could replace a conventional operating system. It is the way the project approaches software as a **living collection of connected activities**.

The command interface supplies a common point of access. The directory layout provides places for different kinds of programs. The Store imagines acquiring new software. The user system experiments with identity. Social introduces interaction between users. Games supply content. The GUI explores how the environment might eventually be presented.

Together, those parts express a single design direction:

> **Build the environment first, then let projects live inside it.**

That is what “a hub” means in the context of PyOs. The hub is not one more application in the collection; it is the **framework that gives the collection a home**.

## Source reference index

For readers tracing the design directly to code:

| Design question | Read this source |
| --- | --- |
| Where is the main hub interface? | [`Home/com.py`](Home/com.py) |
| How were other programs launched? | [`Home/com.py`](Home/com.py), commands `run`, `games`, `firefox`, `mkusr` |
| Where is the first application Store? | [`Apps/store.py`](Apps/store.py) |
| How would Store downloads fit into the hub? | [`Apps/store.py`](Apps/store.py), `local_dir = "./Home/Games/Cookie"` |
| Where does user identity appear? | [`Home/usr.py`](Home/usr.py), `whoami` in [`Home/com.py`](Home/com.py) |
| Where are social features explored? | [`Home/social.py`](Home/social.py), [`Home/book.py`](Home/book.py) |
| Which games were included? | [`Home/Games/test.sh`](Home/Games/test.sh), [`Cookie/`](Cookie/) |
| Where is the GUI prototype? | [`gui/guitest.py`](gui/guitest.py) |
| What was the intended runtime? | [`.replit`](.replit), [`pyproject.toml`](pyproject.toml), [`replit.nix`](replit.nix) |
| What changes were recorded at the time? | [`Updates.md`](Updates.md) |

---

**PyOs is an archived original project by Xylin48.** This README documents the surviving implementation, the author's stated intention, and the architectural meaning of the project as a hub. It does not claim that every planned feature was completed or that the archive is a standalone bootable operating system.
