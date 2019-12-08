# Tensorflow-Testing

### Testing Types
<ol>
  <li> Non Functional Testing
    <ol> 
      <li> Install Testing
      <li> Compatibility Testing
      <li> Volume Testing
      <li> Performance Testing
      </ol>
  <li> Functional Testing
    <ol>
      <li> Unit Testing
      <li> Thread Interaction Testing
    </ol>
 </ol>
 
### Assessment of Testing Quality
In this section, we put forth a few remarks on the guidelines that were followed during the
testing procedure.
<ul>
  <li> All of the tests were repeated at least three times on ​ randomised inputs​ in order to
  avoid the stochastic nature of the software.
  <li> The performance tests were timed up to a accuracy of​ 10<sup>-6</sup> precision​ .
  <li> Each unit test is ran ten times and passes only if all ten test cases pass
  <li> We have tried to the best of our capabilities to ascertain the probable causes for
  encountered bugs.</li>
</ul>

### Evaluation of Tensorflow 2.0
We present some thoughts on the new features of Tensorflow2.0
<ul>
  <li> Tensorflow2.0 is significantly less stable than version 1.4 in terms of ease of
  installation, software compatibility, compatibility with CUDA and other GPU drivers.
  <li> We find that Tensorflow2.0 remains a competitive alternative to Numpyv1.17 in terms
  of accuracy, precision and latency/performance.
  <li> Tensorflow2.0 offers significant gains in terms of Eager Execution in this new version.
  Consequently, this proves immensely useful for quick iteration vis-a-vis the graph
  construction. Although PyTorch did offer this feature from it’s inception,
  Tensorflow2.0 is much more optimised in terms of memory usage and it more
  portable across platforms too.
</ul>

### Decision on Tensorflow 2.0
The utility of the new software depends very much on a case-to-case basis. It is highly
beneficial for small-scale research projects working to push the state-of-the-art in Applied ML
problems. But we would be wary of applying it on large-scale machine learning programs in
production serving a large user base due to the above-delineated issues.
