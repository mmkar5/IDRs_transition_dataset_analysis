#!/usr/bin/env bash

grep -E "sequence|derived-binding_mode_disorder_to_order-mobi" -A 1 mobidb_DD.fasta --no-group-separator > modified_mobidb_DD.fasta
grep -E "sequence|derived-binding_mode_disorder_to_order-mobi" -A 1 mobidb_DO.fasta --no-group-separator > modified_mobidb_DO.fasta
