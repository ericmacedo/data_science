kmeans <- function (dataset, ncluster, threshold) {
	
  	dataset <- as.matrix (dataset) # TRANSFORMA PARA MATRIZ
	centers <- sample (1:nrow (dataset), ncluster) # INDICES DOS CENTRÓIDES ARBITRÁRIOS

	clusters <- list() # ESTRUTURA DE DADOS
	
	for (i in 1:ncluster) {
		clusters [i] <- list ()
		clusters [[i]]$Center <- dataset [centers[i], ] # ATRIBUI OS CENTROIDES
		clusters [[i]]$Nodes <- list ()
		clusters [[i]]$CurrentIndex <- 1
	}

	
	divergenceFactor <- threshold + 1
	while (divergenceFactor > threshold) {

		for (i in 1:nrow (dataset)) {
		 
			closestCenter <- list ()
			closestCenter$clusterId <- 1
			closestCenter$distance <- sqrt(
				sum (
					(dataset [i,] - clusters[[1]]$Center)^2
				)
			)

			for (j in 2:ncluster) {
				localDistance <- sqrt (
					sum (
						(dataset[i,] - clusters[[j]]$Center)^2
					)
				)
				if (localDistance < closestCenter$distance ) {
					closestCenter$clusterId <- j
					closestCenter$distance <- localDistance
				}
			}
			clusters[[closestCenter$clusterId]]$Nodes[clusters[[closestCenter$clusterId]]$CurrentIndex] <-  i
		}


		for (i in 1:ncluster) {
			cluster[[i]]$Old 
		}
	}
}
