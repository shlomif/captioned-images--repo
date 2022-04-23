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

use Carp::Always;
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

my $BASENAME = "read-tolkiens-lotr";

sub bn_mutate
{
    my $ref = shift();
    ${$ref} =~ s#-\Q$BASENAME\E((?:\.svg)?\n?)\z#-see-a-meme-only-once$1#
        or die;
    return;
}

sub bn_mutate_not_only_at_the_end
{
    my $ref = shift();
    ${$ref} =~ s#-\Q$BASENAME\E#-see-a-meme-only-once#
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
    path($new_base)->remove_tree();

    $obj->do_system(
        {
            cmd => [ "cp", "-a", "$orig/", $new_base, ],
        },
    );
    my $fn1        = "$new_base/one-does-not-simply-read-tolkiens-lotr.svg";
    my $sfn1       = "$new_base/one-does-not-simply.jpg";
    my $sfn2       = "$new_base/Makefile";
    my $readme_fn1 = "$new_base/README.asciidoc";
    my $fn2        = $fn1;
    bn_mutate( \$fn2 );
    rename( $fn1, $fn2 );
    {
        my $num_changed = 0;
        path($sfn2)->edit_lines_utf8(
            sub {
                if (/\A BASE/x)
                {
                    bn_mutate( \$_ );
                    ++$num_changed;
                }
                return $_;
            },
        );
        die if $num_changed != 1;
    }
    {
        my $num_changed = 0;
        path($readme_fn1)->edit_lines_utf8(
            sub {
                print;
                if (/\Q$BASENAME\E/x)
                {
                    bn_mutate_not_only_at_the_end( \$_ );
                    ++$num_changed;
                }
                return $_;
            },
        );
        die "num_changed == $num_changed" if $num_changed != 2;
    }
    $obj->do_system(
        {
            cmd => [ "git", "add", $fn2, $sfn1, $readme_fn1, $sfn2, ],
        },
    );

    $obj->do_system(
        {
            cmd => [ "git", "clean", "-fx", "$new_base/", ],
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
