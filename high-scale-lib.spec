%{?scl:%scl_package high-scale-lib}
%{!?scl:%global pkg_name %{name}}

Name:          %{?scl_prefix}high-scale-lib
Version:       1.1.4
Release:       8%{?dist}
Summary:       A collection of Concurrent and Highly Scalable Utilities
# Might want to address with upstream to adjust because
# http://creativecommons.org/licenses/publicdomain/ 
# is considered "retired" in place for some other public domain license
# opened: https://github.com/stephenc/high-scale-lib/issues/4
# Thanks to Timothy St. Clair tstclair@redhat.com
License:       Public Domain
URL:           https://github.com/stephenc/high-scale-lib/
Source0:       https://github.com/stephenc/high-scale-lib/archive/high-scale-lib-parent-%{version}.tar.gz

BuildRequires: %{?scl_mvn_prefix}maven-local
BuildRequires: %{?scl_mvn_prefix}mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: %{?scl_mvn_prefix}mvn(org.sonatype.oss:oss-parent:pom:)
%{?scl:BuildRequires: %scl_name-build}
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
%{?scl_enable}
%setup -q -n %{pkg_name}-%{pkg_name}-parent-%{version}

find . -name "*.bat" -delete
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-shade-plugin java_util_concurrent_chm
%pom_remove_plugin :maven-shade-plugin java_util_hashtable

sed -i 's/\r//' README
%{?scl_enable}

%build
%{?scl_enable}
%mvn_build
%{?scl_disable}

%install
%{?scl_enable}
%mvn_install
%{?scl_disable}

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Tue Jul 26 2016 Pavel Raiskup <praiskup@redhat.com> - 1.1.4-8
- simplification
