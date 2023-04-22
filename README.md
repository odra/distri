# Distri

A CLI that shows parsed data from an linux os release file, usually located at /etc/os-release.

## Usage

Showing the CLI version:

```sh
distri version
```

Displaying a distro's info (path defaults to `/etc/os-release`):

```sh
distri display
distri display --path /etc/another-os-release
```

## License

[MIT](./LICENSE)
