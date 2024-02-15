#!/usr/bin/node

// تصدير الوحدة
exports.nbOccurences = function (list, searchElement) {
  const matchingElements = list.filter(function (element) {
    return element === searchElement;
  });

  return matchingElements.length;
};
