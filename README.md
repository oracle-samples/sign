# SIGN

**sign - signing tool for developers**

## Description

Generic signing tool for developers. This is **NOT for use in
production**. All private keys are stored in the clear. This tool is
geared towards a developer that wants to quickly sign things.

## The Problem

The process is rather lengthy for someone that just wants to quickly sign
something. Therefore this tool can sign anything with only a couple of commands.
You can sign a kernel, module, ima-sign, or sign a boot loader with a DB key.

## Getting started

Initial setup:

```
$ sign init-setup
```

This will create all the keys. Afterwards you must reboot and enroll them
through the MOK.  Console access is required for this step.

## Usage

Then all that needs to be done to sign things is:

```
$ sign module <module name>
$ sign kernel <kernel name>
$ sign ima <anything>
$ sign bootloader <efi program>
```

The keys for the ima and bootloader commands are generated, but not
automatically enrolled like the kernel and module keys. If you want to use
IMA, the ima key must be added to your .ima keyring. If you use the bootloader
command, the DB key must be added through the BIOS. It will also generate
custom KEK and PK keys. All public keys can be found in /etc/sign.

If you want to override the default key values look in (/etc/sign/sign.conf),
and create a file called /etc/sign/local.conf and override anything you’d like.

## Uninstall

If you want to uninstall or start over with new keys:

```
$ sign destroy-setup
```

## Commands

##### backup

    Backup both the public and private keys to move to a different machine.
    Don't mix backup files between OL8 and OL9.

##### bootloader \<efiprogram\>

    PE sign a boot loader.

##### destroy-setup

    Unenroll all keys and remove them from the machine. Afterwards you must
    reboot and unenroll them through the MokManager. When rebooting, shim
    will load the MokManager and ask for a password. If root has a usable
    password set, sign reuses it. Otherwise mokutil prompts for a
    MokManager password while creating the request. Console access is
    required for this step.

##### ima \<filename\>

    IMA sign a file

##### init-setup

    Create all the keys. Afterwards you must reboot and enroll them through
    the MokManager. When rebooting, shim will load the MokManager and ask
    for a password. If root has a usable password set, sign reuses it.
    Otherwise mokutil prompts for a MokManager password while creating the
    request. Console access is required for this step. If you are using
    UEK-NEXT kernels, the \"Oracle Linux Test Certificate\" will also be
    enrolled with this step. Only call this once. If you need to start over
    issue the destroy-setup command first.

##### kernel \<kernel name\>

    PE sign a kernel

##### module \<module name\>

     Sign a module

##### restore \<backup-name\>

    Restore a backup generated from a different machine. This can be used in
    place of the init-setup command. Afterwards a reboot is required. Follow
    the same steps as init-setup to enroll the keys within the MokManager.

## Configuration

The default key values are located in /etc/sign/sign.conf. To override
anything in this file, create a custom file called /etc/sign/local.conf
with the value to be overridden.

## IMA keys

The sign program will enroll the IMA CA. The leaf cert must be loaded
into the .ima keyring. The leaf cert is available in
/etc/sign/x509\_ima.der. This could be added to the initram or loaded
after boot.

## PK, KEK, and DB KEYS

The bootloader command signs the file with a DB key. This key must be
added through the UEFI. There is also a KEK and PK key that may be
enrolled into the UEFI too. These keys are located in /etc/sign and are
called db.der, kek.der, and pk.der.

## Contributing

This project welcomes contributions from the community. Before submitting a
pull request, please [review our contribution guide](./CONTRIBUTING.md)

## Security

Please consult the [security guide](./SECURITY.md) for our responsible
security vulnerability disclosure process

## License

Copyright (c) 2024 Oracle and/or its affiliates.

This software is available to you under

SPDX-License-Identifier: GPL-2.0-or-later

Being under the terms of the GNU General Public License version 2 or later.

SPDX-URL: https://spdx.org/licenses/GPL-2.0-or-later.html

See [the license file](./LICENSE.txt) for more details.
