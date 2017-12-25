# cdshelf

Audio CD backup & conversion tool


## License

Copyright (C) 2017
Marcel Schilling

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU Affero General Public License for more details.

You should have received [a copy of the GNU Affero General Public
License](LICENSE) along with this program.
If not, see <http://www.gnu.org/licenses/>.


## Dependencies

 * [Snakemake](https://snakemake.readthedocs.io)
 * [python-discid](https://python-discid.readthedocs.io)
 * [musicbrainzngs](https://python-musicbrainzngs.readthedocs.io)
 * [cdrdao](http://cdrdao.sourceforge.net)
 * [PyYAML](http://pyyaml.org)


## Usage

```sh
cdshelf <command> [<command> ...] [--config <parameter>=<value> [<parameter>=<value>]]
```

The following commands are currently supported:

 * `help` - print help message
 * `pretend_image` -  pretend to create CD image (dry-run)
 * `image` - create CD image
 * `get_metadata` - fetch missing metadata for shelved releases from MusicBrainz
 * `usage` - show usage
 * `license` - print license
 * `discid` - print Disc ID of Audio CD in CD device
 * `device` - print device `cdshelf` will read Audio CDs from
 * `directory` - print `cdshelf` base directory

The following parameters are currently supported:

 * `device` - device to read Audio CDs from (default: detect default device)
 * `directory` - `cdshelf` base directory (default: `'/home/lecram/music'`)
 * `open_submission_url`  - choice on wether (`"yes"`) or not (`"no"` [or
 any other value]) to (attempt to) open the submission URL of an unknown
 Disc ID in the (default) web browser (default: `'yes'`)
 * `tmpdir_prefix` - `cdshelf` temporary directory prefix (default: `'cdshelf.'`)
 * `tmpdir_suffix` - `cdshelf` temporary directory suffix (default: `'.tmpdir'`)
