%{?scl:%scl_package high-scale-lib}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}high-scale-lib
Version:       1.1.4
Release:       10%{?dist}
Summary:       A collection of Concurrent and Highly Scalable Utilities
# Might want to address with upstream to adjust because
# http://creativecommons.org/licenses/publicdomain/ 
# is considered "retired" in place for some other public domain license
# opened: https://github.com/stephenc/high-scale-lib/issues/4
# Thanks to Timothy St. Clair tstclair@redhat.com
License:       Public Domain
URL:           https://github.com/stephenc/%{pkg_name}/
Source0:       https://github.com/stephenc/%{pkg_name}/archive/%{pkg_name}-parent-%{version}.tar.gz

BuildRequires: %{?scl_prefix_maven}maven-local
BuildRequires: %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: %{?scl_prefix_maven}mvn(org.sonatype.oss:oss-parent:pom:)
%{?scl:Requires: %scl_runtime}

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
%setup -q -n %{pkg_name}-%{pkg_name}-parent-%{version}

find . -name "*.bat" -delete
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-shade-plugin java_util_concurrent_chm
%pom_remove_plugin :maven-shade-plugin java_util_hashtable
%{?scl:EOF}

sed -i 's/\r//' README

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Oct 11 2016 Tomas Repik <trepik@redhat.com> - 1.1.4-10
- use standard SCL macros

* Wed Jul 27 2016 Pavel Raiskup <praiskup@redhat.com> - 1.1.4-9
- typofix

* Tue Jul 26 2016 Pavel Raiskup <praiskup@redhat.com> - 1.1.4-8
- simplification
