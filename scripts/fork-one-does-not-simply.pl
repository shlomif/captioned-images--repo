#! /usr/bin/env perl
#
# Short description for fork-one-does-not-simply.pl
#
# Version 0.0.1
# Copyright (C) 2022 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the MIT license.

use strict;
use warnings;
use 5.014;
use autodie;

use Getopt::Long qw/ GetOptions /;
use Path::Tiny qw/ cwd path tempdir tempfile /;
use Docker::CLI::Wrapper::Container v0.0.4 ();

sub mutate
{
    my $ref = shift();
    ${$ref} =~ s#-Read-LotR\z#-See-a-Meme-Only-Once#
        or die;
    return;
}

sub run
{
    my $output_fn;

    my $obj = Docker::CLI::Wrapper::Container->new(
        { container => "rinutils--deb--test-build", sys => "debian:sid", } );

    if (0)
    {
        GetOptions( "output|o=s" => \$output_fn, )
            or die "errror in cmdline args: $!";

        if ( !defined($output_fn) )
        {
            die "Output filename not specified! Use the -o|--output flag!";
        }
    }
    my $orig     = "One-does-not-Simply-Read-LotR";
    my $new_base = $orig;
    mutate( \$new_base );

    $obj->do_system(
        {
            cmd => [ "cp", "-a", "$orig/", $new_base, ],
        },
    );

    exit(0);
}

run();

1;

__END__

=encoding UTF-8

=head1 NAME

XML::Grammar::Screenplay::App::FromProto

=head1 VERSION

version v0.16.0

=head1 COPYRIGHT AND LICENSE

This software is Copyright (c) 2007 by Shlomi Fish.

This is free software, licensed under:

  The MIT (X11) License

=cut
