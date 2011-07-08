%define glib2_version 2.6.0

Summary: Interfaces for accessibility support
Name: atk
Version: 1.28.0
Release: 2%{?dist}
License: LGPLv2+
Group: System Environment/Libraries
Source: http://download.gnome.org/sources/atk/1.28/atk-%{version}.tar.bz2
URL: http://developer.gnome.org/projects/gap/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gnome-doc-utils
BuildRequires: gettext

%description
The ATK library provides a set of interfaces for adding accessibility
support to applications and graphical user interface toolkits. By
supporting the ATK interfaces, an application or toolkit can be used
with tools such as screen readers, magnifiers, and alternative input
devices.

%package devel
Summary: Development files for the ATK accessibility toolkit
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel >= %{glib2_version}
Requires: pkgconfig
Requires: gtk-doc

%description devel
This package includes libraries, header files, and developer documentation 
needed for development of applications or toolkits which use ATK.

%prep
%setup -q

%build
%configure --disable-gtk-doc
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang atk10

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f atk10.lang
%defattr(-, root, root)
%doc README AUTHORS COPYING NEWS
%{_libdir}/libatk*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/libatk*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/atk

%changelog
* Wed Dec  2 2009 Matthias Clasen <mclasen@redhat.com> - 1.28.0-2
- Drop unneeded BR

* Wed Sep 23 2009 Matthias Clasen <mclasen@redhat.com> - 1.28.0-1
- Update to 2.28.0

* Mon Aug 10 2009 Matthias Clasen <mclasen@redhat.com> - 1.27.90-1
- Update to 2.27.90

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 1.25.2-1
- Update to 2.25.2

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 1.24.0-2
- Tweak %%summary and %%description

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 1.24.0-1
- Update to 1.24.0

* Mon Jul 21 2008 Matthias Clasen <mclasen@redhat.com> - 1.23.5-1
- Update to 1.23.5

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 1.22.0-1
- Update to 1.22.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.92-1
- Update to 1.21.92

* Fri Feb  8 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.5-2
- Rebuild for gcc 4.3

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> - 1.21.5-1
- Update to 1.21.5

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 1.20.0-1
- Update to 1.20.0

* Wed Aug 15 2007 Matthias Clasen <mclasen@redhat.com> - 1.19.6-3
- Small fixes

* Mon Aug  6 2007 Matthias Clasen <mclasen@redhat.com> - 1.19.6-2
- Update license field

* Mon Jul 30 2007 Matthias Clasen <mclasen@redhat.com> - 1.19.6-1
- Update to 1.19.6

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 1.19.3-1
- Update to 1.19.3

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 1.19.1-1
- Update to 1.19.1

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 1.18.0-1
- Update to 1.18.0

* Tue Feb 13 2007 Matthias Clasen <mclasen@redhat.com> - 1.17.0-1
- Update to 1.17.0

* Wed Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 1.13.2-1
- Update to 1.13.2

* Wed Jan 10 2007 Matthias Clasen <mclasen@redhat.com> - 1.13.1-1
- Update to 1.13.1

* Tue Dec 19 2006 Matthias Clasen <mclasen@redhat.com> - 1.12.4-1
- Update to 1.12.4

* Fri Oct 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.12.3-1
- Update to 1.12.3
- Require pkgconfig in the -devel package

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 1.12.2-1.fc6
- Update to 1.12.2

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 1.12.1-2
- Rebuild

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> - 1.12.1-1
- Update to 1.12.1

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.11.4-4.1
- rebuild

* Thu Jun  8 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.4-4
- Rebuild

* Thu Jun  1 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.4-3
- Rebuild

* Tue Apr  4 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.4-2
- Update to 1.11.4

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.3-1
- Update to 1.11.3

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.11.2-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.11.2-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 17 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.2-1
- Update to 1.11.2

* Mon Jan 16 2006 Matthias Clasen <mclasen@redhat.com> - 1.11.0-1
- Update to 1.11.0

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Sep  7 2005 Matthias Clasen <mclasen@redhat.com> - 1.10.3-1
- Update to 1.10.3

* Tue Jun 28 2005 Matthias Clasen <mclasen@redhat.com> - 1.10.1-1
- Update to 1.10.1

* Mon Mar 14 2005 Matthias Clasen <mclasen@redhat.com> - 1.9.1-1
- Update to 1.9.1

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> - 1.9.0-2
- Rebuilt

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> - 1.9.0-1
- update to 1.9.0

* Tue Oct 12 2004 Matthias Clasen <mclasen@redhat.com> - 1.8.0-2
- convert tamil translations to UTF-8 (#135343)

* Wed Sep 22 2004 Matthias Clasen <mclasen@redhat.com> - 1.8.0-1
- update to 2.8.0

* Mon Aug 16 2004 Matthias Clasen <mclasen@redhat.com> - 1.7.3-2
- Remove unnecessary BuildPrereqs

* Fri Jul 30 2004 Matthias Clasen <clasen@redhat.com> 1.7.3-1
- update to 2.7.3

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 1.6.0-1
- update to 2.6.0

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Mark McLoughlin <markmc@redhat.com> 1.5.5-1
- Update to 1.5.5.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 23 2004 Jonathan Blandford <jrb@redhat.com> 1.5.2-1
- new version

* Tue Sep  9 2003 Jonathan Blandford <jrb@redhat.com> 1.4.0-1
- new version

* Tue Aug 19 2003 Jonathan Blandford <jrb@redhat.com> 1.3.5-1
- new version for 2.4

* Wed Jul  9 2003 Owen Taylor <otaylor@redhat.com> 1.2.4-3.0
- Remove specific version requirement from libtool

* Tue Jul  8 2003 Owen Taylor <otaylor@redhat.com> 1.2.4-2.0
- Bump for rebuild

* Tue Jun 10 2003 Owen Taylor <otaylor@redhat.com> 1.2.4-1
- Version 1.2.4

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 20 2002 Owen Taylor <otaylor@redhat.com>
- Package documentation, instead of blowing it away
- Version 1.2.0

* Wed Nov 27 2002 Tim Powers <timp@redhat.com> 1.0.3-3
- remove unpackaged files from the buildroot

* Mon Oct  7 2002 Havoc Pennington <hp@redhat.com>
- require glib 2.0.6-3

* Wed Jul 31 2002 Owen Taylor <otaylor@redhat.com>
- Remove fixed-ltmain.sh
- Version 1.0.3

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 04 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue Jun  4 2002 Havoc Pennington <hp@redhat.com>
- 1.0.2

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr 24 2002 Havoc Pennington <hp@redhat.com>
 - rebuild in different environment

* Wed Apr  3 2002 Alex Larsson <alexl@redhat.com>
- Update to version 1.0.1

* Fri Mar  8 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.0.0

* Mon Feb 25 2002 Alex Larsson <alexl@redhat.com>
- Update to 0.13

* Thu Feb 21 2002 Alex Larsson <alexl@redhat.com>
- Bump for rebuild

* Mon Feb 18 2002 Havoc Pennington <hp@redhat.com>
- rebuild for glib 1.3.14

* Fri Feb 15 2002 Havoc Pennington <hp@redhat.com>
- add horrible buildrequires hack

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 0.12.90 cvs snap

* Tue Jan 29 2002 Owen Taylor <otaylor@redhat.com>
- Version 0.10

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- new snap 0.8.90

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- rebuild with glib hacked to work on 64-bit

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- Version 0.7
- add explicit check for required glib2 version before we do the build,
  so we don't end up with bad RPMs on --nodeps builds

* Fri Oct 26 2001 Havoc Pennington <hp@redhat.com>
- rebuild due to hosage on ia64 build system causing link to old glib

* Thu Oct 25 2001 Owen Taylor <otaylor@redhat.com>
- Version 0.6

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- 0.5
- sync with Owen's version

* Wed Sep 19 2001 Havoc Pennington <hp@redhat.com>
- 0.4
- fix requires
- --enable-static
- put static libs back in file list

* Mon Sep 10 2001 Havoc Pennington <hp@redhat.com>
- update to CVS snapshot

* Wed Sep 05 2001 Havoc Pennington <hp@redhat.com>
- require specific pango version
- fix ltmain.sh to destroy all relinking BS

* Tue Sep  4 2001 root <root@dhcpd37.meridian.redhat.com>
- Version 0.2

* Sat Jul 21 2001 Owen Taylor <otaylor@redhat.com>
- Configure with --disable-gtk-doc

* Tue Jul 10 2001 Trond Eivind Glomsrod <teg@redhat.com>
- Add post- and postun-sections running ldconfig

* Wed Jun 13 2001 Havoc Pennington <hp@redhat.com>
- 0.2

* Fri May  4 2001 Owen Taylor <otaylor@redhat.com>
- Initial version
