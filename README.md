# GDScript to Python to C Transpiler

[![Template](https://github.com/LinuxUserGD/gdscript-transpiler-bin/actions/workflows/template.yml/badge.svg?branch=dev)](https://github.com/LinuxUserGD/gdscript-transpiler-bin/actions/workflows/template.yml)
[![Godot 4.1.dev](Godot-v4.1.svg)](https://downloads.tuxfamily.org/godotengine/4.0/)
[![MIT license](blue.svg)](LICENSE)
[![Python](python.svg)](https://www.python.org/)

[![Icon](icon.svg)](icon.svg) 

- GDScript compiler (using [Nuitka](https://github.com/Nuitka/Nuitka))
- GDScript runtime environment (using [x-python](https://github.com/rocky/x-python))

Minimal Scripts can be transpiled to Python.

Binary builds are compiled using [GitHub Actions](https://github.com/LinuxUserGD/GDScript2PythonTranspiler/actions) for Alpine Linux, macOS and Windows x86_64.

Also see [generated Python source from GDScript](https://github.com/LinuxUserGD/gdscript-transpiler-source).


[![Video](preview.gif)](preview.gif)

## Example

```
git clone --recursive https://codeberg.org/LinuxUserGD/gdscript-transpiler-bin.git && cd gdscript-transpiler-bin
```

### Godot Engine 4 command line (stage0)

- `./godot4 -s bin/gds.gd --quit --headless help`

- `./godot4 -s bin/gds.gd --quit --headless run=bin/gds.gd` (for running GDScript directly using x-python)

- `./godot4 -s bin/gds.gd --quit --headless format=bin/gds.gd` (for generating Python project)

- `./godot4 -s bin/gds.gd --quit --headless compile=bin/gds.gd` (for compiling GDScript to binary using Clang/Nuitka)

### Python environment (stage1)
Installing python gds
```
python -m pip install git+https://github.com/LinuxUserGD/gdscript-transpiler-source.git
```

- `python -m gds help`

- `python -m gds run=bin/gds.gd`

- `python -m gds format=bin/gds.gd`

- `python -m gds compile=bin/gds.gd`

### Nuitka compiled binary (stage2)
Installing gds binary (available at [itch.io](https://linuxusergd.itch.io/gdscript-transpiler-bin))
```
chmod +x gds
```

- `./gds[.exe] help`

- `./gds[.exe] run=bin/gds.gd`

- `./gds[.exe] format=bin/gds.gd`

- `./gds[.exe] compile=bin/gds.gd`

## Benchmark

Time for running GDScript code:

```gdscript
func string() -> int:
	var x: String = ""
	for i in range(0, 300000):
		x += " "
	return x.length()

func add() -> int:
	var x: int = -100000000
	for i in range(0, 100000000):
		x += 1
	return x
```

|              | Godot      | Python     | Nuitka
|--------------|------------|------------|------------
| benchmark.gd | 11.639s    | 4.678s     | 1.857s

## License

### See [LICENSE](LICENSE) and [CREDITS](CREDITS) (third-party licenses)
