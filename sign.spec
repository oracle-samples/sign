Name:           sign
Version:        0.5
Release:        1%{?_rel}
Summary:        Dev signing tools
BuildArch:      noarch
Packager:	Eric Snowberg <eric.snowberg@oracle.com>

License:        GPLv2+
Source0:        %{name}-%{version}.tar.gz

Requires:       pesign
Requires:	efivar
Requires:	glibc-common
Requires:	mokutil
Requires:	nss-tools
Requires:	binutils
Requires:	gawk
Requires:	coreutils
Requires:	kernel-headers
Requires:	ima-evm-utils
Requires:	openssl
Requires:	kernel-devel
Requires:	tar

%description
Signing Tools for Developers.

%prep
%autosetup

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/sign
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
install -m 755 sign $RPM_BUILD_ROOT/usr/bin
install -m 644 sign.conf $RPM_BUILD_ROOT/etc/sign
install -m 644 sign.1.gz $RPM_BUILD_ROOT/usr/share/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/sign
/etc/sign/sign.conf
/usr/share/man/man1/sign.1.gz

%license LICENSE.txt

%changelog
* Tue Mar 17 2026 Eric Snowberg <eric.snowberg@oracle.com> - 0.5
- Fall back to an interactive MokManager password when root has no usable password hash
* Thu Dec 12 2024 Eric Snowberg <eric.snowberg@oracle.com> - 0.4
- Fix init-setup problem that originated from shellcheck change
* Tue Nov 26 2024 Eric Snowberg <eric.snowberg@oracle.com> - 0.3
- Add tar dependency
* Wed Sep 4 2024 Eric Snowberg <eric.snowberg@oracle.com>
- Add license info
* Wed Mar 20 2024 Eric Snowberg <eric.snowberg@oracle.com>
- Add man page
* Fri Feb 23 2024 Eric Snowberg <eric.snowberg@oracle.com>
- Add kernel-devel as a prereq
- IMA fix to be compatible with newer upstream kernels
* Thu Oct 5 2023 Eric Snowberg <eric.snowberg@oracle.com>
- Initial checkin
