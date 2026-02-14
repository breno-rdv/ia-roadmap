# VAEs (Variational Autoencoders)

VAEs are a class of generative models that learn to encode data into a latent space and decode it back to generate new data.

## How They Work

### Encoder (Recognition Network)
- Takes input data (e.g., image) as input
- Compresses data into a latent representation
- Outputs mean (μ) and standard deviation (σ) of latent distribution
- Goal: learn a compressed representation of data

### Latent Space
- Continuous probability distribution (typically Gaussian)
- Enables smooth interpolation between data points
- Allows sampling for generation
- Lower dimensional than input data

### Decoder (Generative Network)
- Takes latent vector as input
- Reconstructs the original data
- Outputs reconstructed data sample
- Goal: accurately recreate input from latent code

### Training Process
1. Encoder compresses input → latent distribution
2. Sample from latent distribution
3. Decoder reconstructs from sample
4. Minimize reconstruction loss + KL divergence regularization
5. Balance between accurate reconstruction and prior matching

## Key Characteristics

| Aspect | Details |
|--------|---------|
| **Training** | Unsupervised learning with probabilistic framework |
| **Generation** | Sample from latent space → decode to output |
| **Quality** | Good but blurrier than GANs/Diffusion models |
| **Diversity** | High diversity, explores full latent space |
| **Stability** | Very stable, easy to train |
| **Interpretability** | Interpretable latent space with meaningful dimensions |
| **Architecture** | Symmetric encoder-decoder with shared structure |

## Mathematical Foundation

```
ELBO (Evidence Lower Bound):
L = E_q[log p(x|z)] - KL(q(z|x) || p(z))
    └─ Reconstruction ─┘   └─ Regularization ─┘

KL Divergence: KL(q(z|x) || p(z)) = -∫ q(z|x) log(p(z)/q(z|x)) dz

Reparameterization Trick: z = μ + σ ⊙ ε, where ε ~ N(0, I)
```

## Popular VAE Variants

### Standard Variants
- **β-VAE** - Disentangled representations (weighted KL)
- **Conditional VAE (CVAE)** - Class-conditional generation
- **Hierarchical VAE** - Multi-level latent hierarchy
- **Ladder VAE** - Skip connections between encoder/decoder

### Advanced Models
- **VQ-VAE** - Vector Quantized VAE (discrete latents)
- **VQ-VAE-2** - Improved hierarchical version
- **Wasserstein VAE (WVAE)** - Better posterior matching
- **Adversarial VAE (AAVAE)** - Combines VAE with adversarial training

## Why They're Powerful

✓ Stable and easy to train  
✓ Interpretable latent space with smooth interpolation  
✓ Generates diverse outputs  
✓ Unsupervised learning from data  
✓ Can perform downstream tasks (classification, clustering)  
✓ Continuous latent representations enable interpolation  
✓ Principled probabilistic framework  

## Advantages vs Other Models

### vs GANs
- ✓ More stable training
- ✓ Easier to train
- ✓ Interpretable latent space
- ✗ Blurrier outputs
- ✗ Lower image quality
- ✗ Slower generation (encoder required)

### vs Diffusion Models
- ✓ Much faster generation
- ✓ Stable training
- ✓ Interpretable latent space
- ✗ Lower quality outputs
- ✗ Blurrier reconstructions
- ✗ Less flexible conditioning

### vs Autoregressive Models
- ✓ Faster generation
- ✓ Better for high-dimensional data
- ✓ Continuous latent space
- ✗ No explicit likelihood model
- ✗ Less interpretable at sequence level

## Challenges

⚠ **Blurry Outputs** - VAEs tend to produce blurry images due to MSE loss  
⚠ **Posterior Collapse** - KL term goes to zero, latent space unused  
⚠ **KL-Reconstruction Tradeoff** - Balancing both objectives is difficult  
⚠ **Limited Diversity** - May collapse to single mode despite continuous latent  
⚠ **Quality vs Diversity** - Higher quality often means less diversity  

## Implementation Considerations

- **Loss Weighting**: Balance reconstruction and KL terms (β parameter)
- **Latent Dimension**: Control trade-off between quality and compression
- **Activation Functions**: ReLU can lead to dead neurons
- **Batch Normalization**: Can interfere with KL divergence
- **Learning Rates**: Standard rates usually work well
- **Posterior Collapse Prevention**: Annealing schedule, free bits, β-scheduling

## Use Cases

- **Data Compression** - Efficient latent representation
- **Anomaly Detection** - High reconstruction error = anomaly
- **Image Interpolation** - Smooth transitions between images
- **Disentangled Representation Learning** - Interpretable factors of variation
- **Data Augmentation** - Generate synthetic training data
- **Semi-supervised Learning** - With limited labeled data

## Resources

- Original Paper: "Auto-Encoding Variational Bayes" (Kingma & Welling, 2013)
- β-VAE: https://openreview.net/forum?id=Sy2fzU9gl
- VQ-VAE: https://arxiv.org/abs/1711.00937
- PyTorch VAE Implementation: https://github.com/AntixK/PyTorch-VAE
- TensorFlow VAE Tutorial: https://www.tensorflow.org/tutorials/generative/cvae