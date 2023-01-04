# Hopfield
### Languages: Python
### GUI tool: Tkinter
<p> All traing and testing data can be found in the folder: <b>Dataset</b></p>
<p><b>The training data must to be correspond with the testing data.</b></p>
<p> For example: If the training data is <i>Basic_Training</i>, then the testing data need to be <i>Basic_Testing</i>.</p>
<p>This project contains 4 files:</p>
<ul>
  <li>Hopfield_training.py: Traing the hopfield network, get the network weight</li>
  <li>Hopfield_testing.py: Use the pre-training weight to recall the pattern correctly.</li>
  <li>Hopfield_TK.py: Control the GUI actions</li>
  <li>change.py: Randomly change the traing data pattern with 1 to space, space to 1. Each element change with the possibility 0.25</li>
</ul>

<p><b>GUI</b></p>
<p> Users can choose the training data and testing data in the combobox respectively.</p>
<p>Press button <i>Start Traing</i> to start train the network and recall the test data pattern.</p>
<p>In the middle of the GUI, users can see the training data pattern and the testing data pattern before recalling and testing data pattern after recalling.</p>
<p>Press the <i>Reset</i> button to clear the text field, users can retrain new data pattern.</p>
