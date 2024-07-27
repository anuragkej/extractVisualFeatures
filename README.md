## Instructions

Resize each image to (100,100)

The extracted visual features should be the whole `last_hidden_state`. That is, for each image, you will extract a W x H x C tensor, where W and H are spatial resolutions and C is the number of channels.

Compute the element-wise average visual features for each of the 2 images (become a single visual feature). That is, the feature vector for each image will be C-dimensional.

Perform L2 normalization on each feature vector.
Sum each element in the average visual feature to a number. That is, you will get two numbers, one for each image.

# Input Image -> Patch Embedding -> Transformer Layers -> Last Hidden State (shows most refined transformer layer)
