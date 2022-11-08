#include <dirent.h>
#include <stdio.h>

int main(void){
   DIR *dirp;
   struct dirent* de;
   dirp = opendir(".");
   while(de = readdir(dirp)) // Yes, one '='.
        printf("%s\n", de->d_name);
   closedir(dirp);
   return 0;
}
