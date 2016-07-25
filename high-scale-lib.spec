Name:          high-scale-lib
Version:       1.1.4
Release:       7%{?dist}
Summary:       A collection of Concurrent and Highly Scalable Utilities
# Might want to address with upstream to adjust because
# http://creativecommons.org/licenses/publicdomain/ 
# is considered "retired" in place for some other public domain license
# opened: https://github.com/stephenc/high-scale-lib/issues/4
# Thanks to Timothy St. Clair tstclair@redhat.com
License:       Public Domain
URL:           https://github.com/stephenc/high-scale-lib/
Source0:       https://github.com/stephenc/high-scale-lib/archive/%{name}-parent-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch

%description
A collection of Concurrent and Highly Scalable Utilities. These
are intended as direct replacements for the java.util.* or
java.util.concurrent.* collections but with better performance
when many CPUs are using the collection concurrently.

This package contains a Mavenized fork of http://high-scale-lib.sourceforge.net/

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}

find . -name "*.bat" -delete
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-shade-plugin java_util_concurrent_chm
%pom_remove_plugin :maven-shade-plugin java_util_hashtable

sed -i 's/\r//' README

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 1.1.4-7
- add missing build requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 05 2015 gil cattaneo <puntogil@libero.it> 1.1.4-4
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.1.4-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Aug 14 2013 gil cattaneo <puntogil@libero.it> 1.1.4-1
- initial rpm
