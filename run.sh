#!/bin/bash
. ./path.sh
datadir=exp_data
lang_dir=lang_dir/lm
extract_features=true
train=true
if $extract_features; then
	# Extract train features
	steps/make_mfcc.sh \
		--mfcc-config conf/mfcc.conf \
		--nj 6 \
		--write-utt2num-frames true \
		--write-utt2dur true \
		$datadir/train \
		$datadir/train/logs \
		$datadir/train
	# Optionally, add CMVN
	  #steps/compute_cmvn_stats_perutt.sh exp_data/train exp_data/train/cmvn_log exp_data/train
	# Extract test features
	steps/make_mfcc.sh \
		--mfcc-config conf/mfcc.conf \
		--nj 1 \
		--write-utt2num-frames true \
		--write-utt2dur true \
		$datadir/test \
		$datadir/test/logs \
		$datadir/test
		add-deltas ark:$datadir/test/raw_mfcc_test.1.ark ark:test_feats.ark
	#steps/compute_cmvn_stats_perutt.sh exp_data/test exp_data/test/cmvn_log exp_data/test
fi

if $train; then
	stage=1
	if [ $stage -le 1 ]; then
		dir=exp/mono_train
		rm -r $dir
		steps/train_mono.sh --norm-vars true --boost-silence 1.5 --nj 6 --cmd run.pl \
					${datadir}/train $lang_dir exp/mono_train || exit 1;
		utils/mkgraph.sh $lang_dir exp/mono_train exp/mono_train/graph || exit 1;
		gmm-copy --binary=false exp/mono_train/final.mdl exp/mono_train/final.mdl.txt
		# Decode test
		steps/decode.sh --nj 6 \
		exp/mono_train/graph exp_data/test exp/mono_train/decode_test
		steps/get_ctm.sh --frame-shift 1 exp_data/test $lang_dir exp/mono_train/decode_test 
		# Show info about the final model
		gmm-info exp/mono_train/final.mdl
	fi
fi
