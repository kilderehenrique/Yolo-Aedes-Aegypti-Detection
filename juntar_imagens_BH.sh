declare -i i=1

mkdir -p datasets/BH-POOLS/images/
mkdir -p datasets/BH-POOLS/annotations/
mkdir -p datasets/BH-WATERTANKS/images/
mkdir -p datasets/BH-WATERTANKS/annotations/

cd datasets/

cd ./BH-DATASET/BH-POOLS/REGION_1/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P1_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_2/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P2_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_3/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P3_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_4/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P4_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_5/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P5_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_6/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P6_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_7/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P7_"$j"; i+=1; done 
cd ../../..
cd ./BH-POOLS/REGION_8/IMAGES/
for j in *; do cp "$j" ../../../../BH-POOLS/images/P8_"$j"; i+=1; done

cd ../../..
cd ./BH-WATERTANKS/REGION_1/IMAGES/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/images/W1_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_2/IMAGES/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/images/W2_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_3/IMAGES/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/images/W3_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_4/IMAGES/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/images/W4_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_5/IMAGES/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/images/W5_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_6/IMAGES/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/images/W6_"$j"; i+=1; done

# Para se ajustar a quantidade que foi copiada
# Faltam 2 de watertanks dando 348
i=$i-1;
echo $i "images"

i=1

cd ../../..
cd ./BH-POOLS/REGION_1/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P1_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_2/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P2_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_3/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P3_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_4/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P4_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_5/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P5_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_6/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P6_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_7/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P7_"$j"; i+=1; done 
cd ../../..
cd ./BH-POOLS/REGION_8/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations/P8_"$j"; i+=1; done

cd ../../..
cd ./BH-WATERTANKS/REGION_1/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations/W1_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_2/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations/W2_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_3/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations/W3_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_4/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations/W4_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_5/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations/W5_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_6/ANNOTATION/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations/W6_"$j"; i+=1; done

# Annotation color

i=1

cd ../../..
cd ./BH-POOLS/REGION_1/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P1_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_2/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P2_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_3/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P3_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_4/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P4_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_5/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P5_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_6/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P6_"$j"; i+=1; done
cd ../../..
cd ./BH-POOLS/REGION_7/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P7_"$j"; i+=1; done 
cd ../../..
cd ./BH-POOLS/REGION_8/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-POOLS/annotations_color/P8_"$j"; i+=1; done

cd ../../..
cd ./BH-WATERTANKS/REGION_1/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations_color/W1_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_2/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations_color/W2_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_3/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations_color/W3_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_4/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations_color/W4_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_5/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations_color/W5_"$j"; i+=1; done
cd ../../..
cd ./BH-WATERTANKS/REGION_6/ANNOTATION_COLOR/
for j in *; do cp "$j" ../../../../BH-WATERTANKS/annotations_color/W6_"$j"; i+=1; done

# Para se ajustar a quantidade que foi copiada
i=$i-1;
echo $i "annotations"