# Shodan FTP Search

This tool searches for public read and / or writeable FTPServers on shodan.

## Usage

```
$ ftpsearch --help
Usage: ftpsearch [OPTIONS]

  CLI Entrypoint.

Options:
  --debug / --no-debug
  --port INTEGER        [default: 21]
  --country TEXT        Country Code  [default: AT]
  --rcode INTEGER       FTP server return code  [default: 230]
  --output TEXT         [default: data]
  --apikey TEXT
  --help                Show this message and exit.
```

To use the default query `230 country:"AT" port:"21"` just call `ftpsearch`.

Output will be in a folder called `data`, but can be overriden with `--output`.


## Development / Installation

```
git clone https://github.com/b3n4kh/shodan-ftpsearch.git
cd shodan-ftpsearch
pip install -e .
```

