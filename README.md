# Seldinger Phase 7b healthcare-CV evaluation-harness public release

Attribution: Colin Son, Seldinger, Inc., ORCID 0000-0002-1782-0537

This cleaned release contains public/non-PHI reproducibility material for the selected real Seldinger Phase 7 run `phase7-experiment-20260715T080239Z-f7ae7d96` / work order `wo-41abfb21e290b725`.

## What is included

- Small derived CSV tables under `data/`.
- Publication figures under `figures/`.
- `scripts/reproduce_tables_figures.py`, which regenerates the public summary figures from the derived CSVs.
- `environment.yml`.
- `public_manifest.json` with exact public dataset identifiers and download commands.

## What is not included

No credentials, no PHI, no private clinical data, no raw MedMNIST NPZ files, no model checkpoints, no provider logs with secrets, no local private filesystem paths, and no oversized scratch artifacts are included.

## Reproduce public figures

```bash
conda env create -f environment.yml
conda activate seldinger-phase7b-public
python scripts/reproduce_tables_figures.py
```

## Public datasets

The selected run used public MedMNIST v2 datasets via the Hugging Face mirror `albertvillanova/medmnist-v2`:

- `data/chestmnist.npz`
- `data/octmnist.npz`
- `data/organamnist.npz`

Download commands and split notes are in `public_manifest.json`. Cite MedMNIST v2: Yang et al., Scientific Data 2023, doi:10.1038/s41597-022-01721-8.

## Scope

The release supports the preprint's bounded claim: simple public-data probe representations showed dataset-dependent discrimination and calibration/failure behavior. It does not include BiomedCLIP/OpenCLIP/DINOv2 embeddings; those were explicitly missing in the selected artifacts and are listed as follow-up work.
