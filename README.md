# Stable Diffusion 2 parser
> Simple application to test Stable Diffusion 2.

## Installation

OS X & Linux (using virtual environment):

```sh
git clone https://github.com/tamagusko/stable-diffusion-2
python -m venv venv
source venv
pip install -r requirements.txt
```

## Usage example

Usage:  
```sh
python text2image.py --text "Prompt to generate image" --filename "output_filename"
```

Example:  
```sh
python text2image.py --text "A black cat with blue eyes" --filename "cat"
```

## Release History

* 0.1.0
    * First release

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

---

© 2022 Tiago Tamagusko.

Open Source Project distributed under the MIT license. See [LICENSE](LICENSE) for details.
